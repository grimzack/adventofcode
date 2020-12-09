package com.advent.day7;

import java.io.File;
import java.io.FileNotFoundException;
import java.util.ArrayDeque;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.HashSet;
import java.util.List;
import java.util.Map;
import java.util.Queue;
import java.util.Scanner;
import java.util.Set;
import java.util.Stack;

public class Day7 {
    public static void partOne() throws FileNotFoundException {
        List<String> bagRules = getBagRules();
        List<BagRule> nodes = new ArrayList<>();

        for (String rule : bagRules) {
            BagRule node = new BagRule(rule);
            nodes.add(node);
        }

        int numOuterBags = findNumOuterBags(nodes);
        System.out.println("Answer to Day 7 Part 1 = " + numOuterBags);
    }

    public static void partTwo() throws FileNotFoundException {
        List<String> bagRules = getBagRules();
        List<BagRule> nodes = new ArrayList<>();

        for (String rule : bagRules) {
            BagRule node = new BagRule(rule);
            nodes.add(node);
        }

        int numInnerBags = findTotalNumberBags(nodes);

        System.out.println("Answer to Day 7 Part 2 = " + numInnerBags);
    }

    private static List<String> getBagRules() throws FileNotFoundException {
        List<String> result = new ArrayList<>();
        Scanner scanner =
                new Scanner(
                        new File("/Users/zackgrim/Documents/adventofcode/2020/src/com/advent/data/day7.input")
                );

        scanner.useDelimiter("\\n");

        while (scanner.hasNext()) {
            result.add(scanner.next());
        }
        return result;
    }

    private static int findNumOuterBags(List<BagRule> rules) {
        Stack<String> colorsToVisit = new Stack<>();
        Set<String> visitedColors = new HashSet<>();
        String curColor;
        colorsToVisit.push("shiny gold");
        int numOuterBags = 0;

        while (!colorsToVisit.empty()) {
            curColor = colorsToVisit.pop();
            visitedColors.add(curColor);
            for (BagRule rule : rules) {
                if (rule.getContents().containsKey(curColor)) {
                    if (!visitedColors.contains(rule.getBagColor())) {
                        colorsToVisit.push(rule.getBagColor());
                        numOuterBags++;
                    }
                }
            }
        }

        return numOuterBags;
    }

    private static int findTotalNumberBags(List<BagRule> rules) {
        Queue<String> colorsToVisit = new ArrayDeque<>();

        Map<String, Integer> totalBagsContained = new HashMap<>();
        for (BagRule r : rules) {
            if (r.getContents().keySet().isEmpty()) {
                colorsToVisit.add(r.getBagColor());
            }
        }

        String curColor;

        while (!colorsToVisit.isEmpty()) {
            curColor = colorsToVisit.remove();

            for (BagRule rule : rules) {
                if (rule.getBagColor().equals(curColor)) {
                    int bagsContained = 0;
                    boolean goodBag = true;
                    for (String child : rule.getContents().keySet()) {
                        if (totalBagsContained.containsKey(child))
                            bagsContained += (totalBagsContained.get(child) * rule.getContents().get(child));
                        else {
                            colorsToVisit.add(curColor);
                            goodBag = false;
                        }
                    }

                    if (goodBag) {
                        totalBagsContained.put(curColor, bagsContained + 1);
                        String finalCurColor = curColor;
                        rules.stream().filter(r -> isParent(finalCurColor, r))
                                .forEach(parent -> colorsToVisit.add(parent.getBagColor()));
                    }
                }
            }
        }

        return totalBagsContained.get("shiny gold") - 1;
    }

    private static boolean isParent(String color, BagRule rule) {
        return (rule.getContents().containsKey(color));
    }
}
