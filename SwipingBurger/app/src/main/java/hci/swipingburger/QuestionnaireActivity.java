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
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_questionnaire);

        int questionFileId = 0;
        if(getIntent().getIntExtra("requestCode",0) == 2) {
            questionFileId = R.raw.questionnaire_final;
        } else {
            questionFileId = R.raw.questionnaire_task;
        }

        LinkedList<String[]> questions = new LinkedList<String[]>();
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
            RatingBar ratingBar = new RatingBar(this);
            ratingBar.setMax(LIKERT_SCALE_MAX);
            ratingBar.setStepSize(1);

            questionnaireLayout.addView(questionTextView);
            questionnaireLayout.addView(ratingBar);
        }

        Button submitButton = new Button(this);
        submitButton.setText("Submit");
        submitButton.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                // TODO: read and write answers
                Log.i("QuestionnaireActivity", "Ending questionnaire activity.");

                finish();
            }
        });
        questionnaireLayout.addView(submitButton);
    }
}
