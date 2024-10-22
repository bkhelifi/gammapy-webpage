// Licensed under a 3-clause BSD style license - see LICENSE.rst
//
// Load js components
//

function loadComponent(componentId, componentPath) {
    fetch(componentPath)
        .then(response => response.text())
        .then(data => {
            document.getElementById(componentId).innerHTML = data;
        })
        .catch(error => console.error('Error loading component:', error));
}

// Load navbar and footer components
window.onload = function () {
    loadComponent('head-placeholder', 'common-head.html');
    loadComponent('navbar-placeholder', 'navbar.html');
    loadComponent('footer-placeholder', 'footer.html');
};
