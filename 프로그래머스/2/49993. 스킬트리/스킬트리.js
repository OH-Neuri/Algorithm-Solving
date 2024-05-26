function solution(skill, skill_trees) {
    let answer = 0;

    const regExp = new RegExp(`[^${skill}]`,"g");

    skill_trees.forEach(function(item) {
        if( skill.indexOf(item.replace(regExp,'')) === 0 ) {
            ++answer;
        }
    })

    return answer;
}