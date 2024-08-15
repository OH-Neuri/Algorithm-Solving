/**
 * @param {number[]} bills
 * @return {boolean}
 */
var lemonadeChange = function (bills) {
    let money = [0, 0, 0]
    for (let bill of bills) {
        if (bill == 5) money[0] += 1
        if (bill == 10) {
            if (money[0] <= 0) return false
            money[1] += 1
            money[0] -= 1
        }
        if (bill == 20) {
            if (money[0] <= 0) return false
            if (money[0] < 3 && money[1] < 1) return false
            if (money[1]>=1) { 
                money[1] -= 1
                money[0] -= 1
             } else {
                money[0] -=3
            }
        }
    }
    return true
};