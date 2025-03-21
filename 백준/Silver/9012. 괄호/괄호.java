import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());

        for (int i = 0; i < n; i++) {
            String str = br.readLine();
            Boolean bool = true; // 올바른 괄호인가? 확인용 
            int count = 0;
            
            for (char c : str.toCharArray()) {
                if (c == '(') {
                    // s == "(" 는 주소값을 비교함. char은 문자 비고
                    count++;
                } else {
                    count--;
                    if (count < 0) {
                        bool = false;
                        break;
                    }
                }
            }

            if (bool && count == 0) {
                // bool이 참이고, count가 0개면 = 개수가 같으면
                System.out.println("YES");
            } else {
                System.out.println("NO");
            }

        }

    }
}