package com.advent.day5;

import com.advent.Utils;

import java.io.IOException;
import java.util.ArrayList;
import java.util.Collections;
import java.util.List;

public class Day5 {
    public static void partOne() throws IOException {
        List<String> boardingPasses = Utils.getInputAsStrings("day5");

        List<Integer> seatIds = convertPassToIds(boardingPasses);

        System.out.println("Answer to Day 5 Part 1 = " + Collections.max(seatIds));
    }

    public static void partTwo() throws IOException {
        List<String> boardingPasses = Utils.getInputAsStrings("day5");
        List<Integer> passIds = convertPassToIds(boardingPasses);

        Collections.sort(passIds);

        int seatIndex = 0;
        for (int i = 0, j = 1; j < passIds.size(); i++, j++) {
            int diff = Math.abs(passIds.get(i) - passIds.get(j));
            if (diff > 1) {
                seatIndex = i;
                System.out.println("Possible seat between " + passIds.get(i) + " and " + passIds.get(j));
            }
        }

        System.out.println("Answer to Day 5 Part 2 = " + ((passIds.get(seatIndex) + passIds.get(seatIndex + 1)) / 2));
    }

    private static List<Integer> convertPassToIds(List<String> boardingPasses) {
        List<Integer> passIds = new ArrayList<>();

        for (String pass : boardingPasses) {
            passIds.add(calculateSeatId(findRow(pass), findColumn(pass)));
        }

        return passIds;
    }

    private static int findRow(String boardingPass) {
        boardingPass = boardingPass.replaceAll("[LR]", "");
        boardingPass = boardingPass.replace('B', '1');
        boardingPass = boardingPass.replace('F', '0');

        return Integer.parseInt(boardingPass, 2);
    }

    private static int findColumn(String boardingPass) {
        boardingPass = boardingPass.replaceAll("[BF]", "");
        boardingPass = boardingPass.replace('R', '1');
        boardingPass = boardingPass.replace('L', '0');

        return Integer.parseInt(boardingPass, 2);
    }

    private static Integer calculateSeatId(int row, int column) {
        return (row * 8) + column;
    }
}
