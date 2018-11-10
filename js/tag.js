// 标签初始化
(function(){
	const TAGS_UL_ID='tags_ul';
	const TAG_CONTENTS_UL_ID='tag_contents_ul';

	function get_query_string(name) {
		var reg = new RegExp("(^|&|\\?)" + name + "=([^&]*)(&|$)", "i");
		var r = window.location.search.substr(1).match(reg);
		if (r != null) return decodeURIComponent(r[2]); 
		return null;
	}

	function filter_nodes(nodes,nodeName){
		let res=[]
		for(let i=0;i<nodes.length;i++){
			if(nodes[i].nodeName==nodeName){
				res.push(nodes[i])
			}
		}
		return res;
	}

	function switch_tag_func(index){
		let parent_obj=document.getElementById(TAGS_UL_ID);
		let tag_nodes=filter_nodes(parent_obj.childNodes,'LI');
		parent_obj=document.getElementById(TAG_CONTENTS_UL_ID);
		let content_nodes=filter_nodes(parent_obj.childNodes,'LI');
		
		let active_class='active';
		return function(){
			for(let i=0;i<tag_nodes.length;i++){
				let btn=filter_nodes(tag_nodes[i].childNodes,'BUTTON')[0];
				btn.classList.remove(active_class)
				content_nodes[i].style.display='none';
			}
			let btn=filter_nodes(tag_nodes[index].childNodes,'BUTTON')[0];
			btn.classList.add(active_class);
			content_nodes[index].style.display='block';
		}
	}

	let param_tag=get_query_string('tag');
    let parent_obj=document.getElementById(TAGS_UL_ID);
    let nodes=filter_nodes(parent_obj.childNodes,'LI');
    for(let i=0;i<nodes.length;i++){
        let btn=filter_nodes(nodes[i].childNodes,'BUTTON')[0];
        btn.addEventListener('click',switch_tag_func(i));
		if(param_tag!=null){
			btn_tag=btn.innerHTML.substr(0,btn.innerHTML.indexOf('(')).replace(/\s+/g,"");
			if(param_tag==btn_tag){
				btn.click();
			}
		}
    }
})();
