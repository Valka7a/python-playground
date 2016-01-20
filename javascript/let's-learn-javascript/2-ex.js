var pTags = document.getElementsByTagName('p')

firstPTag = pTags[0]

firstPTag.innerHTML = "new paragraph"

firstPTag.innerHTML = "new paragraph contetn"

firstPTag.innerHTML = "new paragraph content"

firstPTag.innerHTML = "new paragraph <strong>content</strong>"

var li = document.querySelector('.done')

li.className // = 'done'
li.className = "" // = ""
li.className = "done" // = "done"
li.className = "done also-done" // = "done also-done"
li.className = "done" // = "done"
li.className = "done also-done also" // = "done also-done also"
li.className = li.className + " special" // = "done also-done also special"
li.className = "" // = ""
li.className = "done also-done also special" // = "done also-done also special"
li.className = li.className.replace("also-done", "") // "done  also special" there have 1 more space in't good
li.classList // = ["done", "also", "special"]
li.classList.add('new')
li.classList // = ["done", "also", "special", "new"]
li.classList.remove('new')
li.classList // = ["done", "also", "special"]

li // = <li class="done  also special">Oranges</li>
li.parentElement // = <ul id="checklist">...</ul>
li.parentElement.parentElement
// ^^^
// <main>
//   <p>..</p>
//     <p class="second"> Paragraph .second</p>
//     <h4>Lists</h4>
//   <ul id="checklist">
//     <li>Apples</li>
//     <li class="done  also special">Oranges</li>
//     <li>Bananas</li>
//     <li>Watermelon</li>
//   </ul>
// </main>

li.parentElement.children
//[ <li>Apples</li>,
//  <li class="done  also special">Oranges</li>,
//  <li>Bananas</li>,
//  <li>Watermelon</li>]

li.parentElement.children[0] // = <li>Apples</li>
li.parentElement.children[0].innerHTML = "Frank" // "Frank"
