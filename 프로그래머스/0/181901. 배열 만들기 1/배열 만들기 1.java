class Solution {
    public int[] solution(int n, int k) {
        // n이하의 정수 중에서 k의 배수를 오름차순으로 정렬
        int[] answer = new int[n / k];
        for(int i = 1; i<= n; i++){
            if (i * k <= n){
                answer[i-1] = i*k;
            }
            
        }
        return answer;
    }
}