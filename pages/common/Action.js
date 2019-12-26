//PJBlog 3 Ajax Action File
//Author:evio
var GetFile = ["Action.asp?action="]
var GetAction = ["Hidden&"]

// 关于 [Hidden] 标签的修复代码
function Hidden(i){
	var TempStr;
	var ajax = new AJAXRequest;
	ajax.get(
			 GetFile[0]+GetAction[0]+"TimeStamp="+new Date().getTime(),
			 function(obj) {
				 TempStr = obj.responseText;
				 if ( TempStr == "1" ){
					 $("hidden1_"+i).style.display = "";
					 $("hidden2_"+i).style.display = "none";
				 }else{
					 $("hidden1_"+i).style.display = "none";
					 $("hidden2_"+i).style.display = "";
				 }
			 }
	 );
}