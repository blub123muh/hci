package hci.swipingburger;

import android.Manifest;
import android.app.Activity;
import android.content.Intent;
import android.content.pm.PackageManager;
import android.net.Uri;
import android.os.Bundle;
import android.os.Environment;
import android.support.v4.app.ActivityCompat;
import android.support.v4.app.Fragment;
import android.support.v4.app.FragmentActivity;
import android.support.v4.app.FragmentManager;
import android.support.v4.app.FragmentStatePagerAdapter;
import android.support.v4.view.PagerAdapter;
import android.support.v4.view.ViewPager;
import android.support.v4.widget.DrawerLayout;
import android.util.Log;
import android.view.View;
import android.widget.AdapterView;
import android.widget.ArrayAdapter;
import android.widget.Button;
import android.widget.ImageButton;
import android.widget.LinearLayout;
import android.widget.ListView;
import android.widget.TextView;

import com.opencsv.CSVWriter;

import java.io.File;
import java.io.FileOutputStream;
import java.io.FileWriter;
import java.io.IOException;
import java.lang.reflect.Array;
import java.text.SimpleDateFormat;
import java.util.LinkedList;
import java.util.Scanner;

public class TreasureHuntFragmentActivity extends FragmentActivity implements TreasureHuntRoomFragment.OnFragmentInteractionListener {
    /**
     * The number of pages (wizard steps) to show in this demo.
     */
    private static final int NUM_PAGES = 20;

    /**
     * The page that a task is started at.
     */
    private static final int STARTING_POSITION = 0;

    /**
     * The pager widget, which handles animation and allows swiping horizontally to access previous
     * and next wizard steps.
     */
    private DisablebleViewPager mPager;

    private DrawerLayout mDrawerLayout;
    private ListView mDrawerList;

    private int currentTask;
    private int currentDoor;

    private String participantId;
    private String navigation;
    private long[][] jumpTimeMs;
    private int[][] jumpInteractions;

    private LinkedList<int[]> tasks;

    /**
     * The pager adapter, which provides the pages to the view pager widget.
     */
    private PagerAdapter mPagerAdapter;

    public void created(int pos, View view) {
        if ((currentDoor == 0 && pos == STARTING_POSITION) || (currentDoor > 0 && pos == tasks.get(currentTask)[currentDoor - 1])) {
            TextView instruction = (TextView) view.findViewById(R.id.instruction);
            instruction.setText("Open door " + tasks.get(currentTask)[currentDoor]);
        }
    }

    private class DrawerItemClickListener implements ListView.OnItemClickListener {
        @Override
        public void onItemClick(AdapterView parent, View view, int position, long id) {
            selectItem(position);
        }
    }

    /**
     * Swaps fragments in the main content view
     */
    private void selectItem(int position) {
        mPager.setCurrentItem(position);
        mDrawerList.setItemChecked(position, true);
        mDrawerLayout.closeDrawer(mDrawerList);
    }


    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_treasure_hunt);

        verifyStoragePermissions(this);

        Intent intent = getIntent();
        navigation = intent.getStringExtra("navigation");
        participantId = intent.getStringExtra("participantId");

        // Instantiate Hamburger Menu
        mDrawerLayout = (DrawerLayout) findViewById(R.id.drawer_layout);
        mDrawerList = (ListView) findViewById(R.id.left_drawer);

        // Set the adapter for the list view
        String[] rooms = new String[NUM_PAGES];
        for (int i = 1; i <= NUM_PAGES; i++) {
            rooms[i - 1] = "Room " + i;
        }
        mDrawerList.setAdapter(new ArrayAdapter<String>(this,
                android.R.layout.simple_list_item_1, rooms));
        // Set the list's click listener
        mDrawerList.setOnItemClickListener(new DrawerItemClickListener());

        if (navigation.equals(MainActivity.SWIPE)) {
            Log.i("MainActivity", "Using swipe gesture. Disable hamburger menu.");
            mDrawerLayout.setDrawerLockMode(DrawerLayout.LOCK_MODE_LOCKED_CLOSED);
        }

        // Instantiate a ViewPager and a PagerAdapter.
        mPager = (DisablebleViewPager) findViewById(R.id.pager);
        mPagerAdapter = new TreasureHuntRoomFragmentAdapter(getSupportFragmentManager());
        mPager.setAdapter(mPagerAdapter);

        if (navigation.equals(MainActivity.HAMBURGER)) {

            Log.i("MainActivity", "Using swipe gesture. Disable swipe.");
            mPager.setPagingEnabled(false);
        }

        tasks = new LinkedList<int[]>();
        int longestTask = 0;
        Scanner scanner = new Scanner(this.getResources().openRawResource(R.raw.tasks));
        while (scanner.hasNextLine()) {
            String singleTaskCsv = scanner.nextLine();
            String[] steps = singleTaskCsv.split(",");

            int[] singleTask = new int[steps.length];
            for (int i = 0; i < singleTask.length; i++) {
                singleTask[i] = Integer.parseInt(steps[i]);
            }
            tasks.add(singleTask);

            if (steps.length > longestTask) {
                longestTask = steps.length;
            }
        }
        scanner.close();

        currentTask = 0;
        currentDoor = 0;

        jumpTimeMs = new long[tasks.size()][longestTask];
        jumpInteractions = new int[tasks.size()][longestTask];

    }

    @Override
    public void onBackPressed() {
        // force that back button is not available
    }

    @Override
    protected void onActivityResult(int requestCode, int resultCode, Intent data) {
        if (requestCode == 1) {
            Log.i("TreasureHuntActivity", "Questionnaire for task has finished.");
            // if there are no more tasks, go to the questionnaire
            if (currentTask == tasks.size() - 1) {
                // TODO: go to questionnaire
                Intent intent = new Intent(TreasureHuntFragmentActivity.this, QuestionnaireActivity.class);
                intent.putExtra("requestCode", 2);
                startActivityForResult(intent, 2);
            } else {
                currentDoor = 0;
                currentTask++;
                mPager.setCurrentItem(STARTING_POSITION);
            }
        }

        if (requestCode == 2) {

            Log.i("TreasureHuntActivity", "Questionnaire for whole experiment has finished. Shutting down this activity");
            /* Checks if external storage is available for read and write */
            if (this.isExternalStorageWritable()) {

                Log.i("TreasureHuntActivity", "External Storage is writeable. Trying to write data.");
                String baseDir = android.os.Environment.getExternalStorageDirectory().getAbsolutePath();
                String fileName = "hciResults.csv";
                String filePath = baseDir + File.separator + fileName;
                File file = new File(filePath);
                CSVWriter writer = null;

                // File exist
                try {
                    if (file.exists() && !file.isDirectory()) {

                        FileWriter mFileWriter = new FileWriter(filePath, true);
                        writer = new CSVWriter(mFileWriter);


                    } else {

                        writer = new CSVWriter(new FileWriter(filePath));

                    }


                String[] text = {"Ship Name", "Scientist Name"};
                writer.writeNext(text);

                writer.close();
                } catch (IOException e) {
                    Log.e("TreasureHuntActivity", "Couldn't write to file.", e);
                }
                Log.i("TreasureHuntActivity", "Successfully wrote data.");

            } else {
                /*Hier muss noch ne Fehlerbehandlung hin, damit wir wissen, falls nicht gespeichert werden kann.*/
                Log.e("TreasureHuntActivity", "Can not save the results, because there is no external storage available.");
            }
            finish();
        }
    }

    @Override
    public void open(int position) {
        if (tasks.get(currentTask)[currentDoor] == position) {

            Log.i("Treasure Hunt", "Door " + position + " was opened.");

            PagerAdapter adapter = mPager.getAdapter();
            Fragment fragment = (Fragment) adapter.instantiateItem(mPager, mPager.getCurrentItem());

            View activeView = fragment.getView();
            ImageButton button = (ImageButton) activeView.findViewById(R.id.doorButton);

            int resourceId;
            // if it was the last door to open, treasure was found
            if (currentDoor == tasks.get(currentTask).length - 1) {
                // last step, display treasure and button for next task
                resourceId = R.drawable.door_opened_failed;

                Button nextTaskButton = new Button(this);
                nextTaskButton.setText("Bewerten");
                nextTaskButton.setOnClickListener(new View.OnClickListener() {
                    @Override
                    public void onClick(View v) {
                        // go to questionnaire for task
                        Intent intent = new Intent(TreasureHuntFragmentActivity.this, QuestionnaireActivity.class);
                        intent.putExtra("requestCode", 1);
                        startActivityForResult(intent, 1);
                    }
                });


                LinearLayout layout = (LinearLayout) activeView.findViewById(R.id.fragment_layout);
                layout.addView(nextTaskButton, 1);
            } else {
                currentDoor = currentDoor + 1;
                resourceId = R.drawable.door_opened;
                TextView instruction = (TextView) activeView.findViewById(R.id.instruction);
                instruction.setText("Open door " + tasks.get(currentTask)[currentDoor]);
            }

            button.setImageResource(resourceId);


        } else {
            //TODO: dont do anything
        }
    }

    /**
     * A simple pager adapter that represents 5 ScreenSlidePageFragment objects, in
     * sequence.
     */
    private class TreasureHuntRoomFragmentAdapter extends FragmentStatePagerAdapter {
        public TreasureHuntRoomFragmentAdapter(FragmentManager fm) {
            super(fm);
        }

        @Override
        public Fragment getItem(int position) {

            return TreasureHuntRoomFragment.newInstance(position);
        }

        @Override
        public int getCount() {
            return NUM_PAGES;
        }
    }

    /*Method which checks weather the external storage can be accessed.*/
    private boolean isExternalStorageWritable() {
        String state = Environment.getExternalStorageState();
        if (Environment.MEDIA_MOUNTED.equals(state)) {
            return true;
        }
        return false;
    }

    // Storage Permissions
    private static final int REQUEST_EXTERNAL_STORAGE = 1;
    private static String[] PERMISSIONS_STORAGE = {
            Manifest.permission.READ_EXTERNAL_STORAGE,
            Manifest.permission.WRITE_EXTERNAL_STORAGE
    };

    /**
     * Checks if the app has permission to write to device storage
     *
     * If the app does not has permission then the user will be prompted to grant permissions
     *
     * @param activity
     */
    public static void verifyStoragePermissions(Activity activity) {
        // Check if we have write permission
        int permission = ActivityCompat.checkSelfPermission(activity, Manifest.permission.WRITE_EXTERNAL_STORAGE);

        if (permission != PackageManager.PERMISSION_GRANTED) {
            // We don't have permission so prompt the user
            ActivityCompat.requestPermissions(
                    activity,
                    PERMISSIONS_STORAGE,
                    REQUEST_EXTERNAL_STORAGE
            );
        }
    }

    @Override
    public void onRequestPermissionsResult(int requestCode,
                                           String permissions[], int[] grantResults) {
        switch (requestCode) {
            case REQUEST_EXTERNAL_STORAGE: {
                // If request is cancelled, the result arrays are empty.
                if (grantResults.length > 0
                        && grantResults[0] == PackageManager.PERMISSION_GRANTED) {

                    // permission was granted, yay! Do the
                    // contacts-related task you need to do.

                } else {

                    // permission denied, boo! Disable the
                    // functionality that depends on this permission.
                }
                return;
            }

            // other 'case' lines to check for other
            // permissions this app might request
        }
    }


}
