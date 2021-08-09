let input = document.getElementById('input')
let h3 = document.getElementById('text')

h3.innerHTML = 'TEST'

input.addEventListener('keypress', (e) => {
    if (e.key === 'Enter') {
        console.log(e.target.value)
        e.target.value = ''
    }

})