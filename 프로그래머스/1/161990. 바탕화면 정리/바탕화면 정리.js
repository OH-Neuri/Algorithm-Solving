function solution(wallpaper) {
    let minX = Infinity
    let minY = Infinity
    let maxX = 0
    let maxY = 0
    
    for(let i = 0; i < wallpaper.length; i++){
        const files = wallpaper[i].split("")
        for(let j = 0; j < files.length; j++){
            if(files[j]==="#"){
                minX = Math.min(minX, j)
                minY = Math.min(minY, i)
                maxX = Math.max(maxX, j+1)
                maxY = Math.max(maxY, i+1)
            }
        }
    }
    
    return [minY, minX, maxY, maxX]
}