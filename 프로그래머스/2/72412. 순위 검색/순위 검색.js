function solution(info, queries) {
    const dataBase = new Map()
    
    //데이터베이스에 넣기
    for (const str of info) {
        const [lang,type,period,food,score] = str.split(" ")
        const key = `${lang}-${type}-${period}-${food}`
        
        if (dataBase.get(key)) dataBase.set(key,[...dataBase.get(key), +score])
        else dataBase.set(key,[+score])
    }
    
    for (const [key,val] of dataBase){
        dataBase.set(key,val.sort((a,b) => a-b))
    }
    
    const seperateQuery = (query) => {
        
        let [lang,type,period,last] = query.split(" and ")
        let [food,score] = last.split(" ")
        
        lang = lang==="-" ? ['cpp','java','python'] : [lang]
        type = type==="-" ? ['backend','frontend'] : [type]
        period = period==="-" ? ['junior','senior'] : [period]
        food = food==="-" ? ['chicken','pizza'] : [food]
        
        let ret = []
        for (const la of lang){
            for (const ty of type) {
                for (const pe of period) {
                    for (const fo of food) {
                        ret.push([`${la}-${ty}-${pe}-${fo}`,+score])
                    }
                }
            }
        }
        return ret
    }
    
    const binarySearch = (list,num) => {
        let [left,right] = [0,list.length-1]
        
        while (left <= right) {
            let mid = ~~((left + right) / 2)
            if (list[mid] === num) {
                while (mid>0 && list[mid-1]===num) mid --
                return mid
            }
            
            if (list[mid] > num) right = mid-1
            else left = mid+1
        }
        return left
    }
    
    
    const ret = queries.map(query =>{
        const newQueryList = seperateQuery(query)
        let sum_ = 0
        
        for (const [newQuery,score] of newQueryList){
            
            const numList = dataBase.get(newQuery)
            sum_ += numList ? numList.length-binarySearch(numList,score) : 0
        }
        
        return sum_
    })
    
    return ret
    
}
