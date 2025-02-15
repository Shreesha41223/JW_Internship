class GasStation {
    public int canCompleteCircuit(int[] gas, int[] cost) {
        int requiredGas = 0, totalCost = 0, currGas = 0, startIndex = 0;

        for (int i = 0; i < gas.length; i++) {
            requiredGas += gas[i];
            totalCost += cost[i];
        }

        if (requiredGas < totalCost) {
            return -1;
        }

        for (int i = 0; i < gas.length; i++) {
            currGas += gas[i] - cost[i];
            if (currGas < 0) {
                currGas = 0;
                startIndex = i + 1;
            }
        }
        return startIndex;
    }
}