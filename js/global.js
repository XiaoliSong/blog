
function switch_sidebar(){
    let sidebar=document.getElementById("sidebar");
    let header=document.getElementById("header");
    let main=document.getElementById("main");
    let switch_btn=document.getElementById('switch_btn')

    let open=true;
    let close_sidebar=function(){
        if(open) return false;
        console.log('close_sidebar');
        sidebar.style.display="none";
        header.style.paddingLeft="0";
        main.style.paddingLeft="0";
        setTimeout(function(){
            switch_btn.style.backgroundImage=getComputedStyle(switch_btn).getPropertyValue("--open_bg");
        },300);
        
        main.removeEventListener("touchstart",switch_func);
        header.removeEventListener("touchstart",switch_func);
        open=true;  
    };

    let open_sidebar=function(){
        if(!open) return false;
        console.log('open_sidebar');
        sidebar.style.display="block";
        header.style.paddingLeft=getComputedStyle(sidebar).getPropertyValue("--mwidth");
        main.style.paddingLeft=getComputedStyle(sidebar).getPropertyValue("--mwidth");
        setTimeout(function(){
            switch_btn.style.backgroundImage=getComputedStyle(switch_btn).getPropertyValue("--close_bg");
        },300);
        
        main.addEventListener("touchstart",switch_func);
        header.addEventListener("touchstart",switch_func);
        open=false;
    };

    //打开则open为true
    let switch_func= function(){
        if(open){
            //打开
            open_sidebar();
        }
        else{
            //关闭
            close_sidebar();
        }
        
    }

    window.onresize=function(){
        let w=window.innerWidth|| document.documentElement.clientWidth|| document.body.clientWidth;
        if(w<750) {
            close_sidebar();
            sidebar.style.display="none";
            header.style.paddingLeft='0';
            main.style.paddingLeft='0';
        }
        else{
            sidebar.style.display="block";
            header.style.paddingLeft=getComputedStyle(sidebar).getPropertyValue("--mwidth");
            main.style.paddingLeft=getComputedStyle(sidebar).getPropertyValue("--mwidth");
        }
    }
    return switch_func;
}


function init(){
    let func=switch_sidebar();
    document.getElementById('switch_btn').addEventListener('click',func);
}

init();