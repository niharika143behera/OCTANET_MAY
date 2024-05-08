let inputs = document.getElementById("inp");
let text = document.querySelector(".text");

function Add(){
    if(inputs.value == ""){
        alert("Please Enter Task");
    } else {
        let newEle = document.createElement("ul");
        newEle.innerHTML = `<input type="checkbox"><span>${inputs.value}</span> <i class="fa-solid fa-trash"></i>`;
        text.appendChild(newEle);
        inputs.value = "";
        newEle.querySelector("i").addEventListener("click", remove);
        newEle.querySelector("input[type='checkbox']").addEventListener("change", markDone);
    }
}

function remove(){
    this.parentElement.remove();
}

function markDone(){
    if(this.checked){
        this.nextElementSibling.style.textDecoration = "line-through";
    } else {
        this.nextElementSibling.style.textDecoration = "none";
    }
}
