package com.advent.day8;

import lombok.Getter;
import lombok.Setter;

import java.util.regex.Matcher;
import java.util.regex.Pattern;

@Getter
@Setter
public class Instruction {
    String instruction;
    int value;
    int timesExecuted;
    boolean wasChanged;

    public Instruction(String str) {
        wasChanged = false;
        timesExecuted = 0;
        int tmpVal;
        Pattern pattern = Pattern.compile("([a-z]{3}) ([+-])([0-9]+).*");
        Matcher matcher = pattern.matcher(str);

        if (matcher.matches()) {
            instruction = matcher.group(1);
            tmpVal = Integer.parseInt(matcher.group(3));
            if (matcher.group(2).equals("-")) tmpVal = -tmpVal;
        } else {
            instruction = "";
            tmpVal = 0;
        }

        value = tmpVal;
    }

}
