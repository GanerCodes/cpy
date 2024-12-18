const [vscode,path,fs] = ["vscode","path","fs"].map(require);

const convertersPath = path.join(__dirname, "selection-☾verter.js");

const openConverters = async _ => {
    const document = await vscode.workspace.openTextDocument(convertersPath);
    vscode.window.showTextDocument(document); }

const getConverters = async _ => {
    let converters;
    try {
        delete require.cache[require.resolve(convertersPath)]
        converters = require(convertersPath)
    } catch (e) {
        if (!fs.existsSync(convertersPath)) {
            await openConverters()
            vscode.window.showErrorMessage(`Please define your custom converters first.`)
        } else {
            await openConverters()
            vscode.window.showErrorMessage(`There's an issue loading the converters: ${e}`) }
        return; }
    
    const converterKeys = Object.getOwnPropertyNames(converters).filter(k => typeof converters[k] === "function");
    return { converters, converterKeys }; }
const callConverter = async converter => {
    const editor = vscode.window.activeTextEditor;
    const selsAndRes = [];
    for (const sel of editor.selections) {
        const selTxt = editor.document.getText(sel);
        try {
            const res = converter(selTxt);
            if (typeof res != "string")
                throw Error(`The ${converter} didn't return a string, instead I got ${res}`);
            selsAndRes.push([sel, res]);
        } catch (e) {
            vscode.window.showErrorMessage(e); } }
    // perform one editor action
    await editor.edit(builder => {
        for (const [sel, res] of selsAndRes)
            builder.replace(sel, res); } ); }

const knownConverters = {}
const addMoonvertersAsCommands = async (context, {converters, converterKeys}) => {
    const wereRegisteredKeys = [...Object.keys(knownConverters)]
    const maybeUnregisterdKeys = [...converterKeys] 
    const alreadyRegisteredKeys = []
    const needToSendToJson = []
    for (const converterKey of maybeUnregisterdKeys) {
        if (wereRegisteredKeys.includes(converterKey)) {
            alreadyRegisteredKeys.push(converterKey);
            continue; }
        const commandName = `moonverter.run ${converterKey}`;
        needToSendToJson.push({commandName, commandTitle: `☾vert ${converterKey}`});
        // update the known converters
        knownConverters[converterKey] = converters[converterKey]
        context.subscriptions.push(
            vscode.commands.registerCommand(
                commandName,
                async _ => {
                    try {
                        await callConverter(knownConverters[converterKey])
                    } catch (error) {
                        vscode.window.showErrorMessage(error.stack)
                        vscode.window.showErrorMessage(error.message) } }) ); }
    registerCommandsToPackageJson(needToSendToJson); };
    // for (const converterKey of wereRegisteredKeys)
    //     if (!alreadyRegisteredKeys.includes(converterKey))
    //         // TODO: unregister (not sure what the VS Code API is for this)

const projectsPackageJsonPath = path.join(__dirname, "..", "package.json");
let jDat;
function registerCommandsToPackageJson(commands) {
    if (!jDat) jDat = JSON.parse(fs.readFileSync(projectsPackageJsonPath, 'utf8'));
    const jOld = JSON.stringify(jDat);
    if (!jDat.contributes) jDat.contributes = {};
    if (!jDat.contributes.commands) jDat.contributes.commands = [];
    commands.forEach(({commandName, commandTitle}) => {
        jDat.contributes.commands = jDat.contributes.commands.filter(x => x.command != commandName)
        jDat.contributes.commands.push({
            "command": commandName,
            "title": commandTitle }); });
    const jNew = JSON.stringify(jDat)
    if (jOld != jNew) {
        fs.writeFileSync(__dirname+"/../package.json", JSON.stringify(jDat, null, 4));
        vscode.window.showInformationMessage(`Reload window to see new commands!`); } }

// this method is called when your extension is activated
// your extension is activated the very first time the command is executed
module.exports = {
    async activate(context) {
        console.log('"Selection ☾verter" is now active!');
        context.subscriptions.push( vscode.commands.registerCommand("moonverter.addMoonverter", openConverters))
        context.subscriptions.push(
            vscode.commands.registerCommand("moonverter.moonvertSelectedText", async _ => {
                if (!vscode.window.activeTextEditor) return; // needs a selection
                
                try {
                    let {converters, converterKeys} = await getConverters();
                    addMoonvertersAsCommands(context, {converters, converterKeys}).catch(vscode.window.showErrorMessage);
                    
                    if (!converterKeys.length) {
                        await openConverters();
                        vscode.window.showErrorMessage("Please define your custom ☾verters first.");
                        return; }

                    const selectedConvertKey = await vscode.window.showQuickPick(converterKeys)
                    if (!selectedConvertKey) return;
                    
                    await callConverter(converters[selectedConvertKey])
                } catch (error) {
                    vscode.window.showErrorMessage(error) } }) );

        // register list of commands
        addMoonvertersAsCommands(context, await getConverters()).catch(vscode.window.showErrorMessage) },
    
    deactivate() {} }