function calcularConstante() {
    var ds = parseFloat(document.getElementById("ds").value);
    var jst = parseFloat(document.getElementById("jst").value);
    var ist = parseFloat(document.getElementById("ist").value);
    var km = ((ds/jst)*ist);
    document.getElementById("km").innerHTML = km;
}

function calcularTHE() {
    var pcm = parseInt(document.getElementById("pcm").value);
    var pci = parseInt(document.getElementById("pci").value);
    var pcad = parseInt(document.getElementById("pcad").value);
    var pcsi = parseInt(document.getElementById("pcsi").value);
    var pcit = parseInt(document.getElementById("pcit").value);
    var the = ((pcm*4)+(pci*6)+(pcad*10)+(pcsi*10)+(pcit*18));
    document.getElementById("the").innerHTML = the;
}
function calcularQP() {
    var the = parseInt(document.getElementById("the").innerHTML);
    var km = parseFloat(document.getElementById("km").innerHTML);
    var qp = Math.ceil(the*km);
    document.getElementById("qp").innerHTML = qp;
    }