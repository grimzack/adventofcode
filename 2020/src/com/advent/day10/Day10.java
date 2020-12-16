package com.advent.day10;

import com.advent.Utils;

import java.io.IOException;
import java.util.Collections;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

public class Day10 {
    private static final String DAY = "day10";
    private static final String SAMPLE = "sample";

    public static void main(String[] args) throws IOException {
        partOne();
        partTwo();
    }

    public static void partOne() throws IOException {
        List<Integer> adapters = Utils.getInputAsInts(DAY);

        // Add charging outlet
        if (!adapters.contains(0)) adapters.add(0);
        Collections.sort(adapters);

        // Add device's built-in adapter
        adapters.add((adapters.get(adapters.size() - 1) + 3));

        // Iterate through and increment key/value map
        Map<Integer, Integer> differences = new HashMap<>();
        int diff;
        for (int i = 0, j = 1; j < adapters.size(); i++, j++) {
            diff = adapters.get(j) - adapters.get(i);
            differences.put(diff, differences.getOrDefault(diff, 0) + 1);
        }

        // return 1jolt * 3jolt
        int answer = differences.get(1) * differences.get(3);
        System.out.println("1-Jolts = " + differences.get(1));
        System.out.println("3-Jolts = " + differences.get(3));

        System.out.println("Answer to Day 10 Part 1 = " + answer);
    }

    public static void partTwo() throws IOException {
        List<Long> adapters = Utils.getInputAsLongs(DAY);

        // Add charging outlet
        if (!adapters.contains(0L)) adapters.add(0L);
        Collections.sort(adapters);
        // Add device's built-in adapter
        adapters.add((adapters.get(adapters.size() - 1) + 3));


        // need to figure out how many paths to the end from each adapter
        Map<Long, Long> pathsToEnd = new HashMap<>();
        pathsToEnd.put(adapters.get(adapters.size() - 1), 1L);

        int start = 0;
        long answer = countStepsToEnd(adapters, start, pathsToEnd);

        System.out.println("Answer to Day 10 Part 2 = " + answer);
    }

    private static long countStepsToEnd(List<Long> data, int startIndex, Map<Long, Long> totalPathCounts) {
        long current = data.get(startIndex);

        if (totalPathCounts.containsKey(current)) {
            return totalPathCounts.get(current);
        }

        long totalPaths = 0L;

        if (data.contains(current + 1)) {
            totalPaths += countStepsToEnd(data, data.indexOf(current + 1), totalPathCounts);
        }

        if (data.contains(current + 2)) {
            totalPaths += countStepsToEnd(data, data.indexOf(current + 2), totalPathCounts);
        }

        if (data.contains(current + 3)) {
            totalPaths += countStepsToEnd(data, data.indexOf(current + 3), totalPathCounts);
        }

        totalPathCounts.put(current, totalPathCounts.getOrDefault(current, 0L) + totalPaths);
        return totalPaths;
    }
}
