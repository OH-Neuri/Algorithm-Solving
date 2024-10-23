const readline = require('readline');

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

const input = [];
rl.on('line', (line) => {
  input.push(line);
}).on('close', () => {
  const [V, E] = input[0].split(' ').map(Number);
  const K = Number(input[1]);

  const graph = Array.from({ length: V + 1 }, () => []);
  const distances = Array(V + 1).fill(Infinity);
  
  // MinHeap 정의
  class MinHeap {
    constructor() {
      this.heap = [];
    }

    push({ vertex, distance }) {
      this.heap.push({ vertex, distance });
      this.bubbleUp();
    }

    bubbleUp() {
      let index = this.heap.length - 1;
      const current = this.heap[index];

      while (index > 0) {
        const parentIndex = Math.floor((index - 1) / 2);
        const parent = this.heap[parentIndex];

        if (parent.distance <= current.distance) break;

        this.heap[index] = parent;
        index = parentIndex;
      }

      this.heap[index] = current;
    }

    pop() {
      const min = this.heap[0];
      const end = this.heap.pop();

      if (this.heap.length > 0) {
        this.heap[0] = end;
        this.sinkDown(0);
      }

      return min;
    }

    sinkDown(index) {
      const length = this.heap.length;
      const element = this.heap[index];

      while (true) {
        let leftChildIdx = 2 * index + 1;
        let rightChildIdx = 2 * index + 2;
        let swap = null;

        if (leftChildIdx < length) {
          let leftChild = this.heap[leftChildIdx];
          if (leftChild.distance < element.distance) {
            swap = leftChildIdx;
          }
        }

        if (rightChildIdx < length) {
          let rightChild = this.heap[rightChildIdx];
          if (
            (swap === null && rightChild.distance < element.distance) ||
            (swap !== null && rightChild.distance < this.heap[swap].distance)
          ) {
            swap = rightChildIdx;
          }
        }

        if (swap === null) break;
        this.heap[index] = this.heap[swap];
        index = swap;
      }

      this.heap[index] = element;
    }

    size() {
      return this.heap.length;
    }
  }

  // 그래프 구성
  for (let i = 2; i < input.length; i++) {
    const [u, v, w] = input[i].split(' ').map(Number);
    graph[u].push({ to: v, weight: w });
  }

  // 다익스트라 알고리즘
  const dijkstra = (start) => {
    const pq = new MinHeap();
    distances[start] = 0;
    pq.push({ vertex: start, distance: 0 });

    while (pq.size() > 0) {
      const { vertex: currentVertex, distance: currentDistance } = pq.pop();

      if (distances[currentVertex] < currentDistance) continue;

      for (const neighbor of graph[currentVertex]) {
        const { to, weight } = neighbor;
        const newDist = currentDistance + weight;

        if (newDist < distances[to]) {
          distances[to] = newDist;
          pq.push({ vertex: to, distance: newDist });
        }
      }
    }
  };

  dijkstra(K);

  // 결과 출력
  for (let i = 1; i <= V; i++) {
    if (distances[i] === Infinity) {
      console.log('INF');
    } else {
      console.log(distances[i]);
    }
  }
});
