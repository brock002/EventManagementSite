document.querySelectorAll('.scroll-event-divs').forEach(item => {
    var parent = item.firstElementChild;
    if (parent.scrollWidth<visualViewport.width) {
        parent.parentElement.lastElementChild.style.display = 'none';
    } else {
        parent.addEventListener('scroll', () => {
            let lft = parent.scrollLeft;
            let rgt = parent.scrollWidth-parent.scrollLeft-parent.clientWidth;
            if (lft==0) {
                parent.parentElement.lastElementChild.firstElementChild.disabled=true;
            } else {
                parent.parentElement.lastElementChild.firstElementChild.disabled=false;
            }
            if (rgt==0) {
                parent.parentElement.lastElementChild.lastElementChild.disabled=true;
            } else {
                parent.parentElement.lastElementChild.lastElementChild.disabled=false;
            }
        })
    }
})

function scrollDivRight(id) {
    var rtBtn = document.getElementById(id);
    var scrollyList = rtBtn.parentElement.parentElement.firstElementChild;
    var scrollright = scrollyList.scrollWidth-scrollyList.scrollLeft-scrollyList.clientWidth-500;
    rtBtn.parentElement.firstElementChild.disabled = false;
    
    scrollyList.scrollBy({
        left: 500,
        behavior: 'smooth'
    });

    console.log(scrollright, scrollyList.scrollWidth, scrollyList.clientWidth);
    if (scrollright<=0) {
        rtBtn.disabled=true;
    } else {
        rtBtn.disabled=false;
    }
}

function scrollDivLeft(id) {
    var ltBtn = document.getElementById(id);
    var scrollyList = ltBtn.parentElement.parentElement.firstElementChild;
    var scrollleft = scrollyList.scrollLeft-500;
    ltBtn.parentElement.lastElementChild.disabled = false;

    scrollyList.scrollBy({
        left: -500,
        behavior: 'smooth'
    });

    console.log(scrollleft, scrollyList.scrollWidth, scrollyList.clientWidth);
    if (scrollleft<=0) {
        ltBtn.disabled=true;
    } else {
        ltBtn.disabled=false;
    }
}