package dataStructure;

import java.io.IOException;
import java.io.InputStreamReader;
import java.io.BufferedReader;
import java.util.ArrayDeque;
import java.util.Deque;
import java.util.StringTokenizer;
import java.util.Queue;
import java.util.LinkedList;

public class QueueAndDeque {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int n = Integer.parseInt(br.readLine());
        StringTokenizer st = new StringTokenizer(br.readLine());

        Queue<Integer> q = new LinkedList<>();      // queue 초기화
        Deque<Integer> dq = new ArrayDeque<>();    // deque 초기화

        // 삽입
        for (int i = 0; i < n; i++) {
            int num = Integer.parseInt(st.nextToken());
            // queue : add(throws Exception), offer(return boolean)
            q.add(num);
            // deque : addFirst / addLast (throws Exception), offerFirst / offerLast(return boolean)
            dq.addFirst(num);
        }

        // 조회
        // queue : element(throws Exception), peek(return null)
        System.out.println(q.element());
        // deque : getFirst / getLast(throws Exception), peekFirst / peekLast(return null)
        System.out.println(dq.getFirst());

        // 삭제
        // queue : remove(throws Exception), poll(return null)
        System.out.println(q.remove());
        // deque : removeFirst / removeLast(throws Exception), pollFirst / pollLast(return null)
        System.out.println(dq.removeFirst());

    }
}
