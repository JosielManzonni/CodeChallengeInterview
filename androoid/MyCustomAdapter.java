package com.example.cesarprova;

import android.app.Activity;
import android.icu.lang.UCharacter;
import android.view.View;
import android.view.ViewGroup;
import android.widget.BaseAdapter;

import java.nio.file.FileAlreadyExistsException;
import java.util.List;

public class MyCustomAdapter extends BaseAdapter {

    private List<String> wordList;
    private List<String> wordListFiltered;
    private final Activity act;//we can replace by context

    public MyCustomAdapter(List<String> wordList, Activity act) {

        this.wordListFiltered = wordList;
        this.wordList = wordList;
        this.act =act;
    }

    private boolean second_challenge_stub(String string)
    {
        return false;
    }

    private boolean third_challenge_stub(String string)
    {
        return false;
    }
    @Override
    public int getCount() {
        return wordListFiltered.size();
    }

    public void filter(String text)
    {
        boolean isToAdd = false;
        wordListFiltered.clear();
        if( text.length()==0)
        {
            wordListFiltered.addAll(wordList);
        } else {
            for (String item : wordList) {

                if (second_challenge_stub(text)) {
                    isToAdd = true;
                } else if (third_challenge_stub(text)) {
                    isToAdd ^= true;
                }

                if(isToAdd)
                {
                    wordListFiltered.add(item);
                }

            }
        }
        notifyDataSetChanged();
    }



    @Override
    public Object getItem(int position) {
        return wordListFiltered.get(position);
    }

    @Override
    public long getItemId(int position) {
        //check if exist
        return position;
    }

    @Override
    public View getView(int position, View convertView, ViewGroup parent) {
        View v = act.getLayoutInflater().inflate( R.layout.content_main, parent, false);
        String item = wordListFiltered.get(position);
        return v;
    }

}
