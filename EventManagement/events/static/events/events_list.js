function fix_scrollers() {
    var tabs = document.querySelectorAll(".scrolling-table");
    for (let i = 0; i < tabs.length; i++) {
        if (tabs[i].scrollWidth<visualViewport.width) {
            tabs[i].parentElement.parentElement.lastElementChild.style.display = 'none';
        }
    }
}

fix_scrollers();