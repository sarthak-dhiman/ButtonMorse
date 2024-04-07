const {BrowserWindow,app} = require ('electron');
const createWindow= () =>{
    const win = new BrowserWindow({
        height:800,
        width:800
    })
}
app.whenReady().then(()=> {
    createWindow();
});