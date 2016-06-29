package hci.swipingburger;

import android.Manifest;
import android.app.Activity;
import android.content.Intent;
import android.content.pm.PackageManager;
import android.content.res.Configuration;
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
import android.support.v7.app.ActionBarDrawerToggle;
import android.support.v7.app.AppCompatActivity;
import android.support.v7.widget.Toolbar;
import android.util.Log;
import android.view.View;
import android.widget.AdapterView;
import android.widget.ArrayAdapter;
import android.widget.Button;
import android.widget.ImageButton;
import android.widget.LinearLayout;
import android.widget.ListView;
import android.widget.RelativeLayout;
import android.widget.TextView;

import com.opencsv.CSVWriter;

import java.io.File;
import java.io.FileWriter;
import java.io.IOException;
import java.util.ArrayList;
import java.util.HashSet;
import java.util.LinkedList;
import java.util.Random;
import java.util.Scanner;

public class TreasureHuntFragmentActivity extends AppCompatActivity implements TreasureHuntRoomFragment.OnFragmentInteractionListener {
    /**
     * The number of pages (wizard steps) to show in this demo.
     */
    private static final int NUM_PAGES = 50;

    /**
     * The page that a task is started at.
     */
    private static final int STARTING_POSITION = 25;

    private static final int NUM_TRAININGS_TASKS = 1;

    /**
     * The pager widget, which handles animation and allows swiping horizontally to access previous
     * and next wizard steps.
     */
    private DisablebleViewPager mPager;

    private DrawerLayout mDrawerLayout;
    private ListView mDrawerList;
    private ActionBarDrawerToggle mDrawerToggle;

    private HashSet<Integer> uncompletedTasks;
    private int currentTask;
    private int currentDoor;
    private long lastTimeStamp;
    private int currentInteractions;

    private String participantId;
    private String navigation;
    private long[][] jumpTimeMs;
    private int[][] jumpInteractions;
    private LinkedList<LinkedList<Integer>> taskQuestionnaireResults;
    private LinkedList<Integer> finalQuestionaireResults;

    private LinkedList<int[]> tasks;
    private ArrayList<Integer> trainingsTasks;

    /**
     * The pager adapter, which provides the pages to the view pager widget.
     */
    private PagerAdapter mPagerAdapter;

    public void created(int pos, View view) {

        setTrainingTextViewVisibility(view);

        if ((currentDoor == 0 && pos == STARTING_POSITION) || (currentDoor > 0 && pos == tasks.get(currentTask)[currentDoor - 1])) {
            TextView instruction = (TextView) view.findViewById(R.id.instruction);
            instruction.setText(getResources().getString(R.string.instruction) + " " + (tasks.get(currentTask)[currentDoor] + 1));
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
    protected void onPostCreate(Bundle savedInstanceState) {
        super.onPostCreate(savedInstanceState);
        if (navigation.equals(MainActivity.HAMBURGER)) {
            mDrawerToggle.syncState();
        }
    }

    @Override
    public void onConfigurationChanged(Configuration newConfig) {
        super.onConfigurationChanged(newConfig);
        if (navigation.equals(MainActivity.HAMBURGER)) {
            mDrawerToggle.onConfigurationChanged(newConfig);
        }
    }

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_treasure_hunt);

        // Instantiate Hamburger Menu
        mDrawerLayout = (DrawerLayout) findViewById(R.id.drawer_layout);
        mDrawerList = (ListView) findViewById(R.id.left_drawer);
        verifyStoragePermissions(this);

        Intent intent = getIntent();
        navigation = intent.getStringExtra("navigation");
        participantId = intent.getStringExtra("participantId");

        if (navigation.equals(MainActivity.HAMBURGER)) {
            Toolbar myToolbar = (Toolbar) findViewById(R.id.my_toolbar);
            setSupportActionBar(myToolbar);

            mDrawerToggle = new ActionBarDrawerToggle(
                    this,                  /* host Activity */
                    mDrawerLayout,         /* DrawerLayout object */
                    myToolbar,  /* nav drawer icon to replace 'Up' caret */
                    R.string.open_drawer,  /* "open drawer" description */
                    R.string.close_drawer /* "close drawer" description */
            );

            // Set the drawer toggle as the DrawerListener
            mDrawerToggle.setDrawerIndicatorEnabled(true);
            mDrawerLayout.addDrawerListener(mDrawerToggle);

            getSupportActionBar().setDisplayHomeAsUpEnabled(true);
            getSupportActionBar().setHomeButtonEnabled(true);
        }


        // Set the adapter for the list view
        String[] rooms = new String[NUM_PAGES];
        for (int i = 1; i <= NUM_PAGES; i++) {
            rooms[i - 1] = getResources().getString(R.string.room) + " " + i;
        }
        mDrawerList.setAdapter(new ArrayAdapter<String>(this,
                android.R.layout.simple_list_item_1, rooms));
        // Set the list's click listener
        mDrawerList.setOnItemClickListener(new DrawerItemClickListener());

        if (navigation.equals(MainActivity.SWIPE)) {
            Log.i("MainActivity", "Using swipe gesture. Disable hamburger menu.");
            enableHamburger(false);
        }

        // Instantiate a ViewPager and a PagerAdapter.
        mPager = (DisablebleViewPager) findViewById(R.id.pager);
        mPagerAdapter = new TreasureHuntRoomFragmentAdapter(getSupportFragmentManager());
        mPager.setAdapter(mPagerAdapter);
        mPager.setCurrentItem(STARTING_POSITION);

        // listen for when a page is selected, which is an interaction in our sense
        mPager.addOnPageChangeListener(new ViewPager.OnPageChangeListener() {
            @Override
            public void onPageScrolled(int position, float positionOffset, int positionOffsetPixels) {
                // we dont care
            }

            @Override
            public void onPageSelected(int position) {
                // we count this as an interaction
                currentInteractions++;

                // we want center the menu at this position
                Log.i("TreasureHuntActivity", "Centering the menu at position " + position + ".");
                Log.v("TreasureHuntActivity", "Y-Position before centering: " + mDrawerList.getScrollY());
                mDrawerList.smoothScrollToPositionFromTop(position, (mDrawerList.getHeight() / 2), 0);
                Log.v("TreasureHuntActivity", "Y-Position after centering: " + mDrawerList.getScrollY());
            }

            @Override
            public void onPageScrollStateChanged(int state) {
                // we dont care
            }
        });

        if (navigation.equals(MainActivity.HAMBURGER)) {

            Log.i("MainActivity", "Using swipe gesture. Disable swipe.");
            enableSwipe(false);

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

        uncompletedTasks = new HashSet<Integer>(makeSequence(0, tasks.size() - 1));
        trainingsTasks = makeSequence(0, NUM_TRAININGS_TASKS - 1);

        currentTask = getNextTask();
        currentDoor = 0;

        jumpTimeMs = new long[tasks.size()][longestTask];
        jumpInteractions = new int[tasks.size()][longestTask];

        finalQuestionaireResults = new LinkedList<Integer>();
        taskQuestionnaireResults = new LinkedList<LinkedList<Integer>>();

        lastTimeStamp = System.currentTimeMillis();

    }

    private void setTrainingTextViewVisibility(View view) {
        TextView trainingTextView = (TextView) view.findViewById(R.id.trainingTextView);
        if (trainingsTasks.contains(currentTask)) {


            trainingTextView.setVisibility(View.VISIBLE);
        } else {
            trainingTextView.setVisibility(View.INVISIBLE);
        }
    }

    private ArrayList<Integer> makeSequence(int begin, int end) {
        ArrayList<Integer> ret = new ArrayList(end - begin + 1);
        for (int i = begin; i <= end; i++) {
            ret.add(i);
        }
        return ret;
    }

    private int getNextTask() {
        int nextTask = -1;

        // check if there is a training task has to be completed first
        for (int i = 0; i < NUM_TRAININGS_TASKS; i++) {
            if (uncompletedTasks.contains(i)) {
                nextTask = i;
                break;
            }
        }

        if (nextTask == -1) {
            int size = uncompletedTasks.size();
            nextTask = new Random().nextInt(size);

            int i = 0;
            for (Integer obj : uncompletedTasks) {
                if (i == nextTask) {
                    nextTask = obj;
                    break;
                }
                i = i + 1;
            }
        }

        uncompletedTasks.remove(nextTask);
        return nextTask;
    }

    @Override
    public void onBackPressed() {
        // force that back button is not available
    }

    private LinkedList<Integer> putResultsInList(Intent data) {
        LinkedList<Integer> list = new LinkedList<Integer>();
        int[] results = data.getIntArrayExtra("results");
        Log.i("TreasureHuntActivity", "Read " + results.length + " data from questionnaire.");
        for (int i = 0; i < results.length; i++) {
            list.add(results[i]);
        }
        return list;
    }

    private void enableSwipe(boolean enable) {
        Log.i("TreausureHuntActivity", "Changing the swipe navigation to: " + enable);
        mPager.setPagingEnabled(enable);
    }

    private void enableHamburger(boolean enable) {
        Log.i("TreausureHuntActivity", "Changing the hamburger menu to: " + enable);
        if (enable == false) {
            mDrawerLayout.setDrawerLockMode(DrawerLayout.LOCK_MODE_LOCKED_CLOSED);
        } else {
            mDrawerLayout.setDrawerLockMode(DrawerLayout.LOCK_MODE_UNLOCKED);
        }
    }

    @Override
    protected void onActivityResult(int requestCode, int resultCode, Intent data) {
        if (requestCode == 1) {
            Log.i("TreasureHuntActivity", "Questionnaire for task has finished.");
            Log.i("TreasureHuntActivity", "Reading questionnaire results of task.");

            LinkedList<Integer> resultsForTaskQuestionnaire = putResultsInList(data);
            taskQuestionnaireResults.add(resultsForTaskQuestionnaire);

            // if there are no more tasks, go to the questionnaire
            if (uncompletedTasks.isEmpty()) {
                // TODO: go to questionnaire
                Intent intent = new Intent(TreasureHuntFragmentActivity.this, QuestionnaireActivity.class);
                intent.putExtra("requestCode", 2);
                startActivityForResult(intent, 2);
            } else {
                currentDoor = 0;
                currentTask = getNextTask();
                mPager.setCurrentItem(STARTING_POSITION);
                lastTimeStamp = System.currentTimeMillis();
                currentInteractions = 0;
            }
        }

        if (requestCode == 2) {

            Log.i("TreasureHuntActivity", "Questionnaire for whole experiment has finished.");
            Log.i("TreasureHuntActivity", "Reading results from final questionnaire.");
            finalQuestionaireResults = putResultsInList(data);

            /* Checks if external storage is available for read and write */
            if (this.isExternalStorageWritable()) {

                Log.i("TreasureHuntActivity", "External Storage is writeable. Trying to write data.");
                Log.i("TreasureHuntActivity", "Trying to write experiment data.");
                writeExperimentData();
                Log.i("TreasureHuntActivity", "Trying to write task specific questionnaire data.");
                writeTaskQuestionnaireData();
                Log.i("TreasureHuntActivity", "Trying to final questionnaire data.");
                writeFinalQuestionnaireData();
                Log.i("TreasureHuntActivity", "Successfully wrote data.");

            } else {
                /*Hier muss noch ne Fehlerbehandlung hin, damit wir wissen, falls nicht gespeichert werden kann.*/
                Log.e("TreasureHuntActivity", "Can not save the results, because there is no external storage available.");
            }
            finish();
        }
    }

    private void writeFinalQuestionnaireData() {
        String baseDir = android.os.Environment.getExternalStorageDirectory().getAbsolutePath();
        String fileName = "final_questionnaire_results.csv";
        String filePath = baseDir + File.separator + fileName;
        File file = new File(filePath);
        CSVWriter writer = null;

        // File exist
        try {
            if (file.exists() && !file.isDirectory()) {

                FileWriter mFileWriter = new FileWriter(filePath, true);
                writer = new CSVWriter(mFileWriter);


            } else {
                Log.i("TreasureHuntActivity", "File for final questionnaire result storage doesn't exist yet. Creating...");
                writer = new CSVWriter(new FileWriter(filePath));
                // write column names
                String[] columnNames = {"navigation", "pid", "qid", "result"};
                writer.writeNext(columnNames, false);
            }

            // write data
            for (int qid = 0; qid < finalQuestionaireResults.size(); qid++) {

                String[] questionData = {navigation, participantId + "", qid + "", finalQuestionaireResults.get(qid) + ""};
                writer.writeNext(questionData, false);
            }

            writer.close();
        } catch (IOException e) {
            Log.e("TreasureHuntActivity", "Couldn't write to file.", e);
        }
    }


    private void writeTaskQuestionnaireData() {
        String baseDir = android.os.Environment.getExternalStorageDirectory().getAbsolutePath();
        String fileName = "task_questionnaire_results.csv";
        String filePath = baseDir + File.separator + fileName;
        File file = new File(filePath);
        CSVWriter writer = null;

        // File exist
        try {
            if (file.exists() && !file.isDirectory()) {

                FileWriter mFileWriter = new FileWriter(filePath, true);
                writer = new CSVWriter(mFileWriter);


            } else {
                Log.i("TreasureHuntActivity", "File for task specific questionnaire result storage doesn't exist yet. Creating...");
                writer = new CSVWriter(new FileWriter(filePath));
                // write column names
                String[] columnNames = {"navigation", "pid", "tid", "qid", "result"};
                writer.writeNext(columnNames, false);
            }

            // write data
            for (int tid = 0; tid < taskQuestionnaireResults.size(); tid++) {
                LinkedList<Integer> questionnaireResultsForTask = taskQuestionnaireResults.get(tid);
                for (int qid = 0; qid < questionnaireResultsForTask.size(); qid++) {

                    String[] questionData = {navigation, participantId + "", tid + "", qid + "", questionnaireResultsForTask.get(qid) + ""};
                    Log.v("TreasureHuntActivity", "Writing questiondata: " + questionData);
                    writer.writeNext(questionData, false);
                }
            }

            writer.close();
        } catch (IOException e) {
            Log.e("TreasureHuntActivity", "Couldn't write to file.", e);
        }
    }

    private void writeExperimentData() {
        String baseDir = android.os.Environment.getExternalStorageDirectory().getAbsolutePath();
        String fileName = "experiment_results.csv";
        String filePath = baseDir + File.separator + fileName;
        File file = new File(filePath);
        CSVWriter writer = null;

        // File exist
        try {
            if (file.exists() && !file.isDirectory()) {

                FileWriter mFileWriter = new FileWriter(filePath, true);
                writer = new CSVWriter(mFileWriter);


            } else {
                Log.i("TreasureHuntActivity", "File for data storage doesn't exist yet. Creating...");
                writer = new CSVWriter(new FileWriter(filePath));
                // write column names
                String[] columnNames = {"navigation", "pid", "tid", "jid", "distance", "n_interactions", "time_ms"};
                writer.writeNext(columnNames, false);
            }

            // write data
            for (int tid = 0; tid < jumpTimeMs.length; tid++) {
                for (int jid = 0; jid < jumpTimeMs[0].length; jid++) {
                    int distance = jid == 0 ? tasks.get(tid)[jid] - STARTING_POSITION : tasks.get(tid)[jid] - tasks.get(tid)[jid - 1];
                    String[] jumpData = {navigation, participantId + "", tid + "", jid + "", distance + "", jumpInteractions[tid][jid] + "", jumpTimeMs[tid][jid] + ""};
                    writer.writeNext(jumpData, false);
                }
            }

            writer.close();
        } catch (IOException e) {
            Log.e("TreasureHuntActivity", "Couldn't write to file.", e);
        }
    }

    @Override
    public void open(int position) {
        if (tasks.get(currentTask)[currentDoor] == position) {
            Log.i("Treasure Hunt", "Door " + position + " was opened.");
            long timeRequired = System.currentTimeMillis() - lastTimeStamp;
            int interactionsRequired = currentInteractions;
            Log.i("Treasure Hunt", "Participant " + participantId + " needed " + timeRequired + "ms and " + interactionsRequired + " interactions for task " + currentTask + " and jump " + currentDoor);
            jumpTimeMs[currentTask][currentDoor] = timeRequired;
            jumpInteractions[currentTask][currentDoor] = interactionsRequired;

            PagerAdapter adapter = mPager.getAdapter();
            Fragment fragment = (Fragment) adapter.instantiateItem(mPager, mPager.getCurrentItem());

            View activeView = fragment.getView();
            ImageButton button = (ImageButton) activeView.findViewById(R.id.doorButton);

            int resourceId;
            // if it was the last door to open, treasure was found
            if (currentDoor == tasks.get(currentTask).length - 1) {
                // last step, display treasure and button for next task
                resourceId = R.drawable.door_treasure;

                // disable the navigation so the participant is forced to press the 'next' button
                enableNavigation(false);

                Button nextTaskButton = new Button(this);
                nextTaskButton.setText(getResources().getString(R.string.next));
                nextTaskButton.setOnClickListener(new View.OnClickListener() {
                    @Override
                    public void onClick(View v) {
                        // turn navigation back on again before starting the questionnaire
                        enableNavigation(true);

                        // go to questionnaire for task
                        Intent intent = new Intent(TreasureHuntFragmentActivity.this, QuestionnaireActivity.class);
                        intent.putExtra("requestCode", 1);
                        startActivityForResult(intent, 1);
                    }
                });


                RelativeLayout layout = (RelativeLayout) activeView.findViewById(R.id.fragment_layout);
                layout.addView(nextTaskButton, 1);
            } else {
                currentDoor++;
                resourceId = R.drawable.door_open;
                TextView instruction = (TextView) activeView.findViewById(R.id.instruction);
                instruction.setText(getResources().getString(R.string.instruction) + " " + (tasks.get(currentTask)[currentDoor] + 1));
                lastTimeStamp = System.currentTimeMillis();
                currentInteractions = 0;
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

    private void enableNavigation(boolean enabled) {
        if (navigation.equals(MainActivity.HAMBURGER)) {
            enableHamburger(enabled);
        } else {
            enableSwipe(enabled);
        }
    }

    // Storage Permissions
    private static final int REQUEST_EXTERNAL_STORAGE = 1;
    private static String[] PERMISSIONS_STORAGE = {
            Manifest.permission.READ_EXTERNAL_STORAGE,
            Manifest.permission.WRITE_EXTERNAL_STORAGE
    };

    /**
     * Checks if the app has permission to write to device storage
     * <p>
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
