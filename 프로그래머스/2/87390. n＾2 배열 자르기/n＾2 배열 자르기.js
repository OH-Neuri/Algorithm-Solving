function solution(n, left, right) {
    const ans = [];

    while (left++ <= right){
        const a = left % n,
              b = Math.ceil(left / n);
        if (!a) ans.push(n)
        else if (a < b) ans.push(b);
        else if (a < n) ans.push(a);
    }

    return ans;
}