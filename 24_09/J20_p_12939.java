class Solution {
    public String solution(String s) {
        String answer = "";
        String[] numbers = s.split(" ");
        int max = Integer.MIN_VALUE;
        int min = Integer.MAX_VALUE;
        
        for (int i = 0; i < numbers.length; i++) {
            int number = Integer.parseInt(numbers[i]);
            if (number > max) {
                max = number;
            }
            if (number < min) {
                min = number;
            }
        }
        answer = min+" "+max;
        return answer;
    }
}