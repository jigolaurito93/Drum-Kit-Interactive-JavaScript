// Target the first button and added an event listener which is the click event and invoke the handleClick function
document.querySelector('button').addEventListener('click',handleClick)

function handleClick() {
    alert('I got clicked!');
}