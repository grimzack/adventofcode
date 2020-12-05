package com.advent.day3;

import com.advent.Utils;

import java.io.IOException;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

public class Day3 {
    private static final String DAY = "day3";
    private static final char TREE_CHAR = '#';

    public static void partOne() throws IOException {
        List<String> input = Utils.getInputAsStrings(DAY);

        System.out.println("Answer to Day 3 Part 1 = " + findTrees(3, 1, input));
    }

    public static void partTwo() throws IOException {
        List<String> input = Utils.getInputAsStrings(DAY);

        List<Integer> colSteps = Arrays.asList(1, 3, 5, 7, 1);
        List<Integer> rowSteps = Arrays.asList(1, 1, 1, 1, 2);

        List<Long> numTreesPerSlope = new ArrayList<>();

        for (int i = 0; i < colSteps.size(); i++) {
            numTreesPerSlope.add((long) findTrees(colSteps.get(i), rowSteps.get(i), input));
        }

        long totalTrees = 1;
        for (long slope : numTreesPerSlope) {
            totalTrees = totalTrees * slope;
        }

        System.out.println("Answer to Day 3 Part 2 = " + totalTrees);
    }

    private static int findTrees(int colStep, int rowStep, List<String> input) {
        int row = 0;
        int column = 0;
        int numTrees = 0;

        String line;

        while (row < input.size()) {
            line = input.get(row);

            if (line.charAt(column) == TREE_CHAR) numTrees++;

            column += colStep;
            if (column >= line.length()) column = column % line.length();
            row += rowStep;
        }

        return numTrees;
    }
}
