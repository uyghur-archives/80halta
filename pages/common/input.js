/*
JavaScript File for Uyghur Input By www.xjprgfan.com
Programmer Mahirjan(Email:mayorvb@gmail.com); 2007.3.15
*/
////////////////////////////////////
var uyghur_OBJ="title,log_Intro,Message,link_Name,SearchContent,name,regname,talk,doc1,tagName,Cate_Name,Cate_Intro,New_Cate_Name,New_Cate_Intro,keyWord,reTitle,testArea,SiteName,blog_Title,blog_master,LinkName,new_LinkName,status_title,status_title,mTitle,HtmlCode,KeyWord,log_Pwtips,log_From,tags,des,Pikir_C,Jawap_C,Inkas_C,replay,evio_KeyWords,evio_Description,blog_KeyWords,blog_Description";
///////////////////////////////////
var u_imu=1;
var uyOBJs;
var ua = navigator.userAgent.toLowerCase();
var u_isIE = ((ua.indexOf("msie") != -1) && (ua.indexOf("opera") == -1) && (ua.indexOf("webtv") == -1)) ;
var u_isGecko = (ua.indexOf("gecko") != -1 && ua.indexOf("safari") == -1) ;
var u_isMaxthon = ((ua.indexOf("msie") != -1) && (ua.indexOf("maxthon") != -1)) ;
uyOBJs=uyghur_OBJ.split(",");
window.onload=init_jaryan;
function init_jaryan(){
	var uInObjs=document.getElementsByTagName("input");
	var uTeObjs=document.getElementsByTagName("textarea");
	if(uInObjs.length>0){
	    for(var i=1;i<=uInObjs.length;i++){
	        if(uInObjs[i-1].type.toLowerCase()=="text"){
	            var uy_barmu=false;
	            for(var j=1;j<=uyOBJs.length;j++){
	                if((uInObjs[i-1].id==uyOBJs[j-1] || uInObjs[i-1].name==uyOBJs[j-1]) && uyOBJs[j-1]!=""){ 
	                    uy_barmu=true;break;}
	            }
	            if(uy_barmu) uInObjs[i-1].onkeypress=Harp;
	        }
	    }
	}
	
	if(uTeObjs.length>0){
	    for(var i=1;i<=uTeObjs.length;i++){
	        	var uy_barmu=false;
	            for(var j=1;j<=uyOBJs.length;j++){
	                if((uTeObjs[i-1].id==uyOBJs[j-1] || uTeObjs[i-1].name==uyOBJs[j-1]) && uyOBJs[j-1]!=""){ 
	                    uy_barmu=true;break;}
	            }
	        if(uy_barmu) uTeObjs[i-1].onkeypress=Harp;
	    }
	}
}
function Harp(e){
    var uObj=this;//event.srcElement;
    var uEvent,Kc;
    if(u_isGecko){
        uEvent=e;
        Kc=uEvent.which;
    }else{
        uEvent=window.event;
        Kc=uEvent.keyCode;
    }
    if(u_isMaxthon){//HOT keys for Maxthon
        if (Kc==2){u_imu=!u_imu;return false;} //Control+B
        else if(Kc==10){uObj.style.direction=uObj.style.direction!="ltr"?"ltr":"rtl"} //Control+J     
        else if(Kc==21){//Contrl+U
            var rng=document.selection.createRange();
            if(clipboardData.getData("Text")!=null)rng.text=ulTouy(clipboardData.getData("Text"));
            return false;
        }
    }
    else if(u_isIE){// HOT keys for IE
        if (Kc==20) {uObj.style.direction=(uObj.style.direction=="ltr")?"rtl":"ltr";return false;}//Cotrol+T
        else if(Kc==11) {u_imu=(u_imu)?0:1;return false;}//Control+K
        else if(Kc==21){//Control+U
            var rng=document.selection.createRange();
            if(clipboardData.getData("Text")!=null)rng.text=ulTouy(clipboardData.getData("Text"));
        }
    }
    else if(u_isGecko){
        if (uEvent.ctrlKey && (Kc==116 || Kc==84)) {uObj.style.direction=uObj.style.direction!="ltr"?"ltr":"rtl";return false;}// Control+T
        else if(uEvent.ctrlKey && (Kc==75 || Kc==107)) {u_imu=!u_imu;return false;}//Control+K
    }
    if (u_imu){
    if (Kc==47) Kc=1574;//("/")
    else if (Kc==63) Kc=1567;//("?")
    else if (Kc==44) Kc=1548;//(",")
    else if (Kc==109 ||Kc==77) Kc=1605;//(m yaki M)
    else if (Kc==110 ||Kc==78) Kc=1606;//(n yaki N)
    else if (Kc==98  ||Kc==66) Kc=1576;//(b yaki B)
    else if (Kc==118 ||Kc==86) Kc=1736;//(v yaki V)
    else if (Kc==99  ||Kc==67) Kc=1594;//(c yaki C)
    else if (Kc==120 ||Kc==88) Kc=1588;//(x yaki X)
    else if (Kc==122 ||Kc==90) Kc=1586;//(z yaki Z)
    else if (Kc==97  ||Kc==65) Kc=1726;//(a yaki A)
    else if (Kc==115 ||Kc==83) Kc=1587;//(s yaki S)
    else if (Kc==100) Kc=1583;//("d")
    else if (Kc==68 ) Kc=1688;//("D")
    else if (Kc==102) Kc=1575;//("f")
    else if (Kc==70 ) Kc=1601;//("F")
    else if (Kc==103) Kc=1749;//("g")
    else if (Kc==71 ) Kc=1711;//("G")
    else if (Kc==104) Kc=1609;//("h")
    else if (Kc==72 ) Kc=1582;//("H")
    else if (Kc==106) Kc=1602;//("j")
    else if (Kc==74 ) Kc=1580;//("J")
    else if (Kc==107) Kc=1603;//("k")
    else if (Kc==75 ) Kc=1734;//("K")
    else if (Kc==108 ||Kc==76) Kc=1604;//(l uaki L)
    else if (Kc==59) Kc=1563;//(";")
    else if (Kc==113 ||Kc==81) Kc=1670;//(q yaki Q)
    else if (Kc==119 ||Kc==87) Kc=1739;//(w yaki W)
    else if (Kc==101 ||Kc==69) Kc=1744;//(e yaki E)
    else if (Kc==114 ||Kc==82) Kc=1585;//(r yaki R)
    else if (Kc==116) Kc=1578;//("t")
    else if (Kc==84) Kc=1600;//("T")
    else if (Kc==121 ||Kc==89) Kc=1610;//(y yaki Y)
    else if (Kc==117 ||Kc==85) Kc=1735;//(u yaki U)
    else if (Kc==105 ||Kc==73) Kc=1709;//(i yaki I)
    else if (Kc==111 ||Kc==79) Kc=1608;//(o yaki O)
    else if (Kc==112 ||Kc==80) Kc=1662;//(p yaki P)
    else Kc=0;
    if (Kc!=0 && !uEvent.ctrlKey){
        if (u_isIE || u_isMaxthon){
            window.event.keyCode=Kc;    
        }
        else if(u_isGecko){
            var selstart = uObj.selectionStart ;
            var selend   = uObj.selectionEnd ;
            var insStr = String.fromCharCode ( Kc ) ;
            uObj.value = uObj.value.substring (0, selstart) + insStr + uObj.value.substr ( selend ) ;
            uObj.setSelectionRange(selstart + insStr.length, selstart + insStr.length );
            return false;            
        }
    }
  }
}
function ulTouy(uStr){
var uText=" " + uStr.toLowerCase();
uText=uText.replace(/ a/g," ئا");
uText=uText.replace(/ e/g," ئە");
uText=uText.replace(/ é/g," ئې");
uText=uText.replace(/ i/g," ئى");
uText=uText.replace(/ o/g," ئو");
uText=uText.replace(/ u/g," ئۇ");
uText=uText.replace(/ ö/g," ئۆ");
uText=uText.replace(/ ü/g," ئۈ");
uText=uText.replace(/a/g,"ا");
uText=uText.replace(/e/g,"ە");
uText=uText.replace(/é/g,"ې");
uText=uText.replace(/i/g,"ى");
uText=uText.replace(/o/g,"و");
uText=uText.replace(/u/g,"ۇ");
uText=uText.replace(/ö/g,"ۆ");
uText=uText.replace(/ü/g,"ۈ");
uText=uText.replace(/sh/g,"ش");
uText=uText.replace(/ng/g,"ڭ");
uText=uText.replace(/gh/g,"غ");
uText=uText.replace(/ch/g,"چ");
uText=uText.replace(/b/g,"ب");
uText=uText.replace(/d/g,"د");
uText=uText.replace(/f/g,"ف");
uText=uText.replace(/g/g,"گ");
uText=uText.replace(/h/g,"ھ");
uText=uText.replace(/j/g,"ج");
uText=uText.replace(/k/g,"ك");
uText=uText.replace(/l/g,"ل");
uText=uText.replace(/m/g,"م");
uText=uText.replace(/n/g,"ن");
uText=uText.replace(/p/g,"پ");
uText=uText.replace(/q/g,"ق");
uText=uText.replace(/r/g,"ر");
uText=uText.replace(/s/g,"س");
uText=uText.replace(/t/g,"ت");
uText=uText.replace(/w/g,"ۋ");
uText=uText.replace(/y/g,"ي");
uText=uText.replace(/z/g,"ز");
uText=uText.replace(/x/g,"خ");
//uText=uText.replace(/,/g,"،");
//uText=uText.replace(/?/g,"؟");
//uText=uText.replace(/;/g,"؛");
return uText;
}