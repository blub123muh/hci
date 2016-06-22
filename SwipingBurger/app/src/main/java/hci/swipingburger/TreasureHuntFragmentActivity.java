package hci.swipingburger;

import android.content.Intent;
import android.net.Uri;
import android.os.Bundle;
import android.support.v4.app.Fragment;
import android.support.v4.app.FragmentActivity;
import android.support.v4.app.FragmentManager;
import android.support.v4.app.FragmentStatePagerAdapter;
import android.support.v4.view.PagerAdapter;
import android.support.v4.view.ViewPager;
import android.util.Log;
import android.view.View;
import android.widget.Button;
import android.widget.ImageButton;
import android.widget.LinearLayout;
import android.widget.TextView;

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
    private ViewPager mPager;

    private int currentTask;
    private int currentDoor;

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

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_screen_slide);

        // Instantiate a ViewPager and a PagerAdapter.
        mPager = (ViewPager) findViewById(R.id.pager);
        mPagerAdapter = new TreasureHuntRoomFragmentAdapter(getSupportFragmentManager());
        mPager.setAdapter(mPagerAdapter);

        tasks = new LinkedList<int[]>();
        Scanner scanner = new Scanner(this.getResources().openRawResource(R.raw.tasks));
        while (scanner.hasNextLine()) {
            String singleTaskCsv = scanner.nextLine();
            String[] steps = singleTaskCsv.split(",");

            int[] singleTask = new int[steps.length];
            for (int i = 0; i < singleTask.length; i++) {
                singleTask[i] = Integer.parseInt(steps[i]);
            }
            tasks.add(singleTask);
        }
        scanner.close();

        currentTask = 0;
        currentDoor = 0;
    }

    @Override
    public void onBackPressed() {
        if (mPager.getCurrentItem() == 0) {
            // If the user is currently looking at the first step, allow the system to handle the
            // Back button. This calls finish() on this activity and pops the back stack.
            super.onBackPressed();
        } else {
            // Otherwise, select the previous step.
            mPager.setCurrentItem(mPager.getCurrentItem() - 1);
        }
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
}
