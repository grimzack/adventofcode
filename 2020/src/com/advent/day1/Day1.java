package com.advent.day1;

import com.advent.Utils;
import com.advent.day2.Day2;

import java.io.IOException;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

public class Day1 {
    private static String DAY = "day1";

    public static void partOne() throws IOException {
        Map<Integer, Integer> inverse2020Map = new HashMap<>();
        List<Integer> input = Utils.getInputAsInts(DAY);

        for (Integer num : input) {
            inverse2020Map.put((2020 - num), num);
        }

        for (Integer num : input) {
            if (inverse2020Map.containsKey(num)) {
                System.out.println("Answer to Day 1 Part 1 = " + (num * inverse2020Map.get(num)));
            }
        }
    }

    public static void partTwo() throws IOException {
        Map<Integer, Integer> inverse2020Map = new HashMap<>();
        List<Integer> input = Utils.getInputAsInts(DAY);

        for (Integer num : input) {
            inverse2020Map.put((2020 - num), num);
        }

        for (int i = 0; i < input.size(); i++) {
            int firstNum = input.get(i);
            for (int secondNum : input) {
                int numSum = firstNum + secondNum;
                if (inverse2020Map.containsKey(numSum)) {
                    System.out.println("Answer to Day 1 Part 2 = " + firstNum * secondNum * inverse2020Map.get(numSum));
                }
            }
        }
    }

}
