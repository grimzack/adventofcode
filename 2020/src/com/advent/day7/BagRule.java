package com.advent.day7;

import lombok.Value;

import java.util.Arrays;
import java.util.HashMap;
import java.util.List;
import java.util.Map;
import java.util.regex.Matcher;
import java.util.regex.Pattern;
import java.util.stream.Collectors;

@Value
public class BagRule {
    String bagColor;
    Map<String, Integer> contents;

    public BagRule(String input) {
        contents = new HashMap<>();

        Pattern colorPattern = Pattern.compile("^([a-z ]*) bags contain (.*).");
        Matcher colorMatcher = colorPattern.matcher(input);
        if (colorMatcher.matches()) {
            bagColor = colorMatcher.group(1);
        } else {
            bagColor = "";
        }

        List<String> numberAndColor = Arrays.stream(colorMatcher.group(2).split(" bag[s]?[ .,]*"))
                .collect(Collectors.toList());

        Pattern numberColorPattern = Pattern.compile("^([0-9]+) ([a-z ]*)$");
        for (String str : numberAndColor) {
            Matcher matcher = numberColorPattern.matcher(str);
            if (matcher.matches()) {
                contents.put(matcher.group(2), Integer.parseInt(matcher.group(1)));
            }
        }
    }
}
