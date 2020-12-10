package com.advent.day9;

import com.advent.Utils;

import java.io.IOException;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collections;
import java.util.List;
import java.util.OptionalLong;

public class Day9 {
    private static final String DAY = "day9";
    private static final String SAMPLE = "sample";

    private static final String INPUT_FILE =
            "/Users/zackgrim/Documents/adventofcode/2020/src/com/advent/data/sample.input";

    public static void main(String[] args) throws IOException {
        partOne();
        partTwo();
    }

    public static Long partOne() throws IOException {
        List<Long> data = Utils.getInputAsLongs(DAY);
        int preamble = 25;

        List<Long> summedPair;
        Long unmatched = 0L;
        for (int i = preamble; i < data.size() - 1; i++) {
            List<Long> preambleList = new ArrayList<>(data.subList(i - preamble, i));
            summedPair = findIfPairExists(preambleList, data.get(i));
            if (summedPair.isEmpty()) {
                unmatched = data.get(i);
                break;
            };
        }

        System.out.println("Answer to Day 9 Part 1 = " + unmatched);
        return unmatched;
    }

    private static List<Long> findIfPairExists(List<Long> input, Long target) {
        Collections.sort(input);

        int smallEndIndex = 0;
        int bigEndIndex = input.size() - 1;

        while (smallEndIndex < bigEndIndex) {
            Long firstNum = input.get(smallEndIndex);
            Long secondNum = input.get(bigEndIndex);
            if (firstNum + secondNum == target) {
                return (Arrays.asList(firstNum, secondNum));
            } else if ((firstNum + secondNum) < target) {
                smallEndIndex++;
            } else if ((firstNum + secondNum) > target) {
                bigEndIndex--;
            }
        }

        return Collections.emptyList();
    }

    public static void partTwo() throws IOException {
        List<Long> data = Utils.getInputAsLongs(DAY);

        Long target = partOne();

        int startingIndex = 0;
        int endIndex = 0;
        Long curSum;

        for (int i = 0; i < data.size(); i++) {
            curSum = data.get(i);
            endIndex = i + 1;
            while (endIndex < data.size() && curSum < target) {
                curSum += data.get(endIndex);
                endIndex++;
            }

            if (curSum.equals(target)) {
                startingIndex = i;
                endIndex--;
                break;
            }
        }

        OptionalLong minimum = data.subList(startingIndex, endIndex + 1).stream().mapToLong(v -> v).min();
        OptionalLong maximum = data.subList(startingIndex, endIndex + 1).stream().mapToLong(v -> v).max();
        System.out.println("Two numbers are: " + minimum + " and " + maximum);

        System.out.println("Answer to Day 9 Part 2 = " + (minimum.getAsLong() + maximum.getAsLong()) );
    }
}
