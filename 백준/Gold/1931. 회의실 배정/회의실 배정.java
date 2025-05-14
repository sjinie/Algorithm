import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Main {
	
	static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
	static int n;
	static Lecture[] Lectures;
	
	public static void main(String[] args) throws NumberFormatException, IOException {
		n = Integer.parseInt(br.readLine());
		Lectures = new Lecture[n];
		
		for(int i=0;i<n;i++) {
			StringTokenizer st = new StringTokenizer(br.readLine());
			int start = Integer.parseInt(st.nextToken());
			int end = Integer.parseInt(st.nextToken());
			Lectures[i] = new Lecture(start,end);
		}
		Arrays.sort(Lectures);
		//종료시간으로 정렬
		
        int count = 0, prevEndTime = 0;
        for (int i=0;i<n;i++) {
        	Lecture target = Lectures[i];
            if (prevEndTime <= target.start) {
                prevEndTime = target.end;
                count++;
            }
        }
        System.out.println(count);
	}

	static class Lecture implements Comparable<Lecture> {
		int start, end;
		
		Lecture(int start, int end){
			this.start = start;
			this.end = end;
		}
		

		@Override
		public int compareTo(Lecture o) {
			return this.end == o.end ? this.start - o.start : this.end - o.end;
		}
	}
}
