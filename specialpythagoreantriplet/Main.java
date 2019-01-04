import java.util.ArrayList;

import com.oracle.jrockit.jfr.Producer;

public class Main {

    static int sumTo = 12; // 3 + 4 + 5
    static int prodTo = 0;

    public static void main(String[] args) {
        if (args.length > 0) {
            sumTo = Integer.parseInt(args[0]);
        }

        ArrayList<int[]> possibleSolutionArrays = new ArrayList<>();

        // generate all arrays of three numbers (A,B and C) that sum to 1000
        // where a < b < c
        // our solution int[3] will exist only in this domain
        for (int c = sumTo - 3; c >= 1; c--) {
            for (int b = c - 1; b >= 1; b--) {
                for (int a = b - 1; a >= 1; a--) {
                    if (a + b + c == sumTo) {
                        possibleSolutionArrays.add(new int[] { a, b, c });
                    }
                }
            }
        }

        for (int[] ps : possibleSolutionArrays) {
            if (Math.pow(ps[0], 2) + Math.pow(ps[1], 2) == Math.pow(ps[2], 2)) {
                System.out.printf("a: %d , b: %d, c: %d \n", ps[0], ps[1], ps[2]);
                System.out.printf("the number is: %d \n", ps[0] * ps[1] * ps[2]);
            }
        }

        System.out.printf("sumTo: %s\n", sumTo);
    }

}