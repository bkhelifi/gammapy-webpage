// Licensed under a 3-clause BSD style license - see LICENSE.rst
//
// Main js file for the site
//

function TodayDate(){
  let dateObj = new Date();
  let month = String(dateObj.getMonth() + 1).padStart(2, '0');
  let day = String(dateObj.getDate()).padStart(2, '0');
  let year = dateObj.getFullYear();
  let output = day + '/' + month + '/' + year;

  // Insert date and time into HTML
  return output

}
document.getElementById("TodayDate").innerHTML = TodayDate();

// Load Matomo
var _paq = window._paq = window._paq || [];
/* Matomo tracker methods like "setCustomDimension" should be called before "trackPageView" */
_paq.push(['trackPageView']);
_paq.push(['enableLinkTracking']);
(function() {
    var u = "https://apcstatview.in2p3.fr/";
    _paq.push(['setTrackerUrl', u + 'matomo.php']);
    _paq.push(['setSiteId', '2']);
    var d = document, g = d.createElement('script'), s = d.getElementsByTagName('script')[0];
    g.async = true;
    g.src = u + 'matomo.js';
    s.parentNode.insertBefore(g, s);
})();

// Load Popper.js
var popperScript = document.createElement('script');
popperScript.src = "https://cdn.jsdelivr.net/npm/@popperjs/core@2.11.6/dist/umd/popper.min.js";
document.head.appendChild(popperScript);

// Load Bootstrap JS
var bootstrapScript = document.createElement('script');
bootstrapScript.src = "https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/js/bootstrap.bundle.min.js";
bootstrapScript.integrity = "sha384-YvpcrYf0tY3lHB60NNkmXc5s9fDVZLESaAA55NDzOxhy9GkcIdslK1eN7N6jIeHz";
bootstrapScript.crossOrigin = "anonymous";
document.head.appendChild(bootstrapScript);
