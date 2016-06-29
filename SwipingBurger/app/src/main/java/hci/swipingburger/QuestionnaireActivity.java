package hci.swipingburger;

import android.content.Intent;
import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.util.Log;
import android.view.View;
import android.widget.Button;
import android.widget.LinearLayout;
import android.widget.RatingBar;
import android.widget.TextView;

import java.util.LinkedList;
import java.util.Scanner;

public class QuestionnaireActivity extends AppCompatActivity {

    public static final int LIKERT_SCALE_MAX = 7;

    private LinkedList<RatingBar> mRatingBars;
    private int resultCode;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_questionnaire);

        mRatingBars = new LinkedList<RatingBar>();
        resultCode = getIntent().getIntExtra("requestCode",0);

        int questionFileId = 0;
        if(resultCode == 2) {
            questionFileId = R.raw.questionnaire_final;
        } else {
            questionFileId = R.raw.questionnaire_task;
        }

        final LinkedList<String[]> questions = new LinkedList<String[]>();
        Scanner scanner = new Scanner(this.getResources().openRawResource(questionFileId));
        while (scanner.hasNextLine()) {
            String singleQuestionCsv = scanner.nextLine();
            String[] steps = singleQuestionCsv.split(",");

            String[] singleQuestion = new String[steps.length];
            for (int i = 0; i < singleQuestion.length; i++) {
                singleQuestion[i] = steps[i];
            }
            questions.add(singleQuestion);
        }
        scanner.close();

        LinearLayout questionnaireLayout = (LinearLayout) findViewById(R.id.questionnaire_layout);
        for (String[] question: questions) {
            TextView questionTextView = new TextView(this);
            questionTextView.setText(question[0]);
            RatingBar ratingBar = (RatingBar) RatingBar.inflate(this, R.layout.ratingbar_layout, null);
            ratingBar.setMax(LIKERT_SCALE_MAX);
            mRatingBars.add(ratingBar);
            Log.i("QuestionnaireActicity", "Number of stars " + ratingBar.getNumStars());
            questionnaireLayout.addView(questionTextView);
            questionnaireLayout.addView(ratingBar);
        }

        Button submitButton = new Button(this);
        submitButton.setText(R.string.next);
        submitButton.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                if(!allRatingsPerformed()) {
                    // don't do anything
                    return;
                }

                Log.i("QuestionnaireActivity", "Ending questionnaire activity.");

                Intent resultData = getIntent();
                int[] results = new int[questions.size()];

                for(int i = 0; i < results.length; i++) {
                    float rating = mRatingBars.get(i).getRating();
                    Log.v("QuestionnaireActivity", "Got rating " + rating + " for question " + i);
                    results[i] = (int) (rating);
                }

                resultData.putExtra("results", results);
                setResult(resultCode, resultData);
                finish();
            }
        });
        questionnaireLayout.addView(submitButton);
    }

    public boolean allRatingsPerformed() {
        for (RatingBar ratingBar: mRatingBars) {
            if(ratingBar.getRating() == 0) {
                return false;
            }
        }
        return true;
    }

    @Override
    public void onBackPressed() {
        // force that back cannot be pressed
    }
}
