package graphTraversal;

import java.io.IOException;
import java.io.InputStreamReader;
import java.io.BufferedReader;
import java.util.StringTokenizer;
import java.util.ArrayList;
import java.util.LinkedList;
import java.util.Queue;

public class DfsAndBfs {
    static ArrayList<Integer>[] graph;
    static boolean[] visited;

    public static void dfs(int start) {
        if (visited[start]) return;

        visited[start] = true;
        System.out.print(start + " ");
        for (int v : graph[start]) {
            if (!visited[v]) {
                dfs(v);
            }
        }
    }

    public static void bfs(int start) {
        Queue<Integer> q = new LinkedList<Integer>();
        q.add(start);
        visited[start] = true;
        while (!q.isEmpty()) {
            int v = q.remove();
            System.out.print(v + " ");
            for (int nv : graph[v]) {
                if (!visited[nv]) {
                    q.add(nv);
                    visited[nv] = true;
                }
            }
        }
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int n = Integer.parseInt(st.nextToken());
        int m = Integer.parseInt(st.nextToken());

        graph = new ArrayList[n];
        for (int i = 0; i < n; i++) {
            graph[i] = new ArrayList<>();
        }

        for (int i = 0; i < m ; i++) {
            st = new StringTokenizer(br.readLine());
            int u = Integer.parseInt(st.nextToken());
            int v = Integer.parseInt(st.nextToken());
            graph[u].add(v);
            graph[v].add(u);
        }

        int start = Integer.parseInt(br.readLine());
        visited = new boolean[n];
        dfs(start);

        visited = new boolean[n];
        bfs(start);
    }
}
