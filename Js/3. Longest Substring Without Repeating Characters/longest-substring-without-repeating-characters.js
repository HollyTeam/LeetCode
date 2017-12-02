/**
 * @param {string} s
 * @return {number}
 */

/**
 * 使用cache来保存已经检测过的不重复字符串的下标，用以减少循环次数
 *
 */

var lengthOfLongestSubstring = function(s) {
    var maxLength = 1;
    var temp = '';
    var sLength = s.length;
    var cache;	//用来保存不一样的角标
    
    if(Object.prototype.toString.call(s) !== '[object String]' || s.length === 0){
    	return 0;
    }
    
    for(var i=0;i<sLength;i++){
    	if(maxLength > (sLength - i)){
    		break;
    	}
    	
        for(var j=i;j<sLength;j++){
        	if(j < cache){
        		j = cache;
        		temp = s.substring(i,j+1);
        		continue;
        	}

            if(temp.indexOf(s[j]) !== -1){   //出现重复字符
               if(maxLength < temp.length){
                   maxLength = temp.length;
                }
                cache = j-1;
                temp = '';
                break; 
            }
            
            temp = temp + s[j];
            
            if(maxLength < temp.length){
                maxLength = temp.length;
            }
        }  
    }
    
    return maxLength;
}