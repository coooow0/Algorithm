import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String numStr = br.readLine();

        int[] arr = new int[numStr.length()];
        for (int i = 0; i < numStr.length(); i++) {
            arr[i] = numStr.charAt(i) - '0';
            // '0'을 하는 이유: charAt()을 하면 아스키코드로 입력이 됨. 그래서 '0'의 아스키 코드 값을 빼주어야 함
        }

        int[] number = new int[10];

        for (int i = 0; i < 10; i++) {
            number[i] = 0;
        }

        for (int n : arr) {
            if (n == 6 || n == 9) {
                if (number[6] >= number[9]) {
                    number[9]++;
                }else{
                    number[6]++;
                }
            }else{
                number[n]++;
            }
        }
//        for (int n : number) {
//            System.out.print(n +" ");
//        }

        int max = number[0];

        for (int i = 1; i < 10; i++) {
            if (max < number[i]) {
                max = number[i];
            }
        }
        System.out.println(max);

    }
}