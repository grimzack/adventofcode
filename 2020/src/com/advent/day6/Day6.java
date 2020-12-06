package com.advent.day6;

import java.io.File;
import java.io.FileNotFoundException;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.HashMap;
import java.util.HashSet;
import java.util.List;
import java.util.Map;
import java.util.Scanner;
import java.util.Set;
import java.util.stream.Collectors;

public class Day6 {
    public static void partOne() throws FileNotFoundException {
        List<String> answers = parseAnswers();

        int numDistinctAnswers = countDistinct(answers);

        System.out.println("Answer to Day 6 Part 1 = " + numDistinctAnswers);
    }

    public static void partTwo() throws FileNotFoundException {
        List<List<String>> answerGroups = parseAnswersIntoGroups();

        int uniqueAnswers = 0;
        for (int i = 0; i < answerGroups.size(); i++) {
            System.out.println("i = " + i);
            System.out.println("answers = " + answerGroups.get(i));

            uniqueAnswers += countUniqueAnswers(answerGroups.get(i));
        }


        System.out.println("Answer to Day 6 Part 2 = " + uniqueAnswers);
    }

    private static int countUniqueAnswers(List<String> strings) {
        Map<Character, Integer> allAnswers = new HashMap<>();
        for (String str : strings) {
            for (char c : str.toCharArray()) {
                int count = allAnswers.getOrDefault(c, 0);
                allAnswers.put(c, count + 1);
            }
        }

        int numAllAnswered = 0;
        for (char ch : allAnswers.keySet()) {
            if (allAnswers.get(ch) == strings.size()) numAllAnswered++;
        }

        return numAllAnswered;
    }

    private static int countDistinct(List<String> answers) {
        int totalDistinct = 0;
        for (String str : answers) {
            Set<Character> charSet = new HashSet<>();
            for (char c : str.toCharArray()) {
                charSet.add(c);
            }
            totalDistinct += charSet.size();
        }

        return totalDistinct;
    }

    private static List<String> parseAnswers() throws FileNotFoundException {
        List<String> result = getAnswers();

        return result.stream().map(str -> str.replace("\n", ""))
                .collect(Collectors.toList());
    }

    private static List<List<String>> parseAnswersIntoGroups() throws FileNotFoundException {
        List<String> result = getAnswers();

        List<List<String>> answersAsGroups = new ArrayList<>();

        for (String str : result) {
            answersAsGroups.add(Arrays.stream(str.split("\n")).collect(Collectors.toList()));
        }

        return answersAsGroups;
    }

    private static List<String> getAnswers() throws FileNotFoundException {
        List<String> result = new ArrayList<>();
        Scanner scanner =
                new Scanner(
                        new File("/Users/zackgrim/Documents/adventofcode/2020/src/com/advent/data/day6.input")
                );

        scanner.useDelimiter("\\n\\n");

        while (scanner.hasNext()) {
            result.add(scanner.next());
        }
        return result;
    }
}
