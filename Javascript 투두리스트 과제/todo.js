document.getElementById('addButton').addEventListener('click',addButton);
document.getElementById('removePart').addEventListener('click',removePart);
document.getElementById('removeLast').addEventListener('click',removeLast);
document.getElementById('removeAll').addEventListener('click',removeAll);


function addButton(){

    const contents=document.querySelector('.addText');

    if(!contents.value){
        
        return 0;
    }

    const tr=document.createElement('tr');
    const input=document.createElement('input')
    input.setAttribute('type','checkbox');
    input.setAttribute('class','checkbtn');
    tr.setAttribute('class','fontColor2'); //세팅

    const td=document.createElement('td');
    td.appendChild(input);
    tr.appendChild(td); //체크박스 붙여줌

    const td2=document.createElement('td');
    td2.innerHTML=contents.value;
    tr.appendChild(td2); //글자 붙여줌

    document.getElementById('tableList').appendChild(tr);
    contents.value=''; //초기화
    contents.focus();

}

function removePart(){

    const tableList = document.getElementById('tableList');
    const checkbtn = document.querySelectorAll('#tableList .checkbtn');


    for(const i in checkbtn) {
        if(checkbtn[i].nodeType == 1 && checkbtn[i].checked == true) 
        {
            tableList.removeChild(checkbtn[i].parentNode.parentNode);
        }
    }
    
}

function removeLast(){


    const tableList=document.getElementById('tableList');
    const list=document.querySelectorAll('#tableList > tr');
    
    if(list.length<=0){
        return 0;
    }

    tableList.removeChild(list[list.length-1]);
    
    
}

function removeAll(){

    const tableList=document.getElementById('tableList');
    while(tableList.firstChild){
        tableList.removeChild(tableList.firstChild);
    }    
}