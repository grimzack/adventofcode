package com.advent.day1;

import java.util.HashMap;
import java.util.List;
import java.util.Map;

public class Day1Part1 {
    public static int findProduct(List<Integer> input) {
        Map<Integer, Integer> inverse2020Map = new HashMap<>();

        for (Integer num : input) {
            inverse2020Map.put((2020 - num), num);
        }

        for (Integer num : input) {
            if (inverse2020Map.containsKey(num)) {
                return (num * inverse2020Map.get(num));
            }
        }

        return 0;
    }
}
