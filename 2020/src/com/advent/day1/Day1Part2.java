package com.advent.day1;

import java.util.HashMap;
import java.util.List;
import java.util.Map;

public class Day1Part2 {
    public static int findProduct(List<Integer> input) {
        Map<Integer, Integer> inverse2020Map = new HashMap<>();

        for (Integer num : input) {
            inverse2020Map.put((2020 - num), num);
        }

        for (int i = 0; i < input.size(); i++) {
            int firstNum = input.get(i);
            for (int j = 0; j < input.size(); j++) {
                int secondNum = input.get(j);
                int numSum = firstNum + secondNum;
                if (inverse2020Map.containsKey(numSum)) {
                    return firstNum * secondNum * inverse2020Map.get(numSum);
                }
            }
        }

        return 0;
    }
}
