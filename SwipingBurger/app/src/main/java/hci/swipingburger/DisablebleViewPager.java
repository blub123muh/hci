package hci.swipingburger;

import android.content.Context;
import android.support.v4.view.ViewPager;
import android.util.AttributeSet;
import android.view.MotionEvent;

/**
 * Created by fmai on 22.06.16.
 */
public class DisablebleViewPager extends ViewPager {

    boolean enablePaging = true;

    public DisablebleViewPager(Context context) {
        super(context);
    }

    public DisablebleViewPager(Context context, AttributeSet attrs) {
        super(context,attrs);
    }

    @Override
    public boolean onTouchEvent(MotionEvent event) {
        if(enablePaging) {
            return super.onTouchEvent(event);
        }
        else {
            return false;
        }
    }

    @Override
    public boolean onInterceptTouchEvent(MotionEvent event) {
        if(enablePaging) {
            return super.onInterceptTouchEvent(event);
        }
        else {
            return false;
        }
    }

    public void setPagingEnabled(boolean b) {
        enablePaging = b;
    }
}
