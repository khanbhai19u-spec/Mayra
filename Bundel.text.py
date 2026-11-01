#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
MAYRA — Your Personal AI Assistant  |  One-file project bundle
Run:   python Bundel.text.py            -> creates ./mayra
       python Bundel.text.py my-folder  -> creates ./my-folder
       python Bundel.text.py --list     -> lists files only
Then upload the folder to GitHub (see mayra/README.md). No zip needed.
"""
import pathlib, sys

FILES = {}

# ───────────────────────── HTML ─────────────────────────
FILES["public/index.html"] = r'''<!doctype html>
<html lang="bn"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">
<meta name="theme-color" content="#0a1a3a">
<title>MAYRA — Your Personal AI Assistant</title>
<link rel="icon" href="assets/logo.svg">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;600;800&family=Hind+Siliguri:wght@400;600&display=swap" rel="stylesheet">
<link rel="stylesheet" href="css/style.css">
</head><body>
<div id="app"></div><div id="toast"></div>
<script type="module" src="js/app.js"></script>
</body></html>
'''

# ───────────────────────── CSS ─────────────────────────
FILES["public/css/style.css"] = r'''
:root{--navy:#0a1a3a;--navy2:#13306b;--acc:#3b82f6;--soft:#e8f0ff;--bg:#f6f8fd;--ink:#0f1b33;--mut:#5b6b8c;--line:#dde5f5;--lvl:0;--r:14px}
*{box-sizing:border-box;margin:0}
html,body{height:100%}
body{font:15px/1.55 "Plus Jakarta Sans","Hind Siliguri",system-ui,sans-serif;background:var(--bg);color:var(--ink);-webkit-tap-highlight-color:transparent}
#app{display:flex;min-height:100dvh}
.i{width:20px;height:20px;fill:none;stroke:currentColor;stroke-width:1.8;stroke-linecap:round;stroke-linejoin:round;flex:none}
h1{font-size:1.5rem;font-weight:800;letter-spacing:-.02em;margin-bottom:.25rem}
h2,h3{font-weight:600;margin-bottom:.5rem}
.sub{color:var(--mut);margin-bottom:1rem}
small{display:block;color:var(--mut);font-size:.82rem}
.grow{flex:1;min-width:0}.row{display:flex;gap:.6rem;flex-wrap:wrap;align-items:center}
.side{display:none;width:250px;background:var(--navy);color:#cfdcff;padding:18px 12px;flex-direction:column;gap:6px;position:sticky;top:0;height:100dvh;overflow:auto}
.brand{display:flex;gap:10px;align-items:center;padding:4px 8px 16px;color:#fff}
.brand img{width:38px;height:38px}.brand b{letter-spacing:.14em}.brand small{color:#8fa8e6;font-size:.7rem}
.side nav{display:flex;flex-direction:column;gap:2px;flex:1}
.side a,.navbtn,.sheet a{display:flex;gap:10px;align-items:center;padding:10px 12px;border-radius:10px;color:inherit;text-decoration:none;background:none;border:0;font:inherit;cursor:pointer;text-align:left}
.side a:hover,.navbtn:hover{background:#ffffff14}.side a.on{background:var(--acc);color:#fff}
.content{flex:1;min-width:0;display:flex;flex-direction:column}
.top{display:flex;gap:10px;align-items:center;padding:calc(10px + env(safe-area-inset-top)) 16px 10px;background:#fff;border-bottom:1px solid var(--line);position:sticky;top:0;z-index:5}
.mic{font-size:.78rem;padding:4px 10px;border-radius:99px;background:var(--soft);color:var(--mut)}
.mic.on{background:#dcfce7;color:#166534}
main{padding:18px 16px 110px;max-width:980px;width:100%;margin:0 auto}
.card{background:#fff;border:1px solid var(--line);border-radius:var(--r);padding:16px;margin-bottom:14px;display:flex;flex-direction:column;gap:10px}
.grid{display:grid;grid-template-columns:repeat(2,1fr);gap:10px;margin:12px 0}
.stat{background:linear-gradient(140deg,var(--navy),var(--navy2));color:#fff;border-radius:var(--r);padding:14px}
.stat b{font-size:1.7rem;display:block}.stat span{color:#a9bdf0;font-size:.82rem}
label{display:flex;flex-direction:column;gap:4px;font-weight:600;font-size:.85rem;color:var(--navy2)}
label:has(input[type=checkbox]){flex-direction:row;align-items:center;gap:8px}
input,select,textarea{font:inherit;padding:10px 12px;border:1px solid var(--line);border-radius:10px;background:#fff;color:var(--ink);width:100%}
input[type=checkbox]{width:auto}
input:focus,select:focus,textarea:focus{outline:2px solid var(--acc);outline-offset:-1px}
.btn{display:inline-flex;gap:8px;align-items:center;justify-content:center;border:1px solid var(--navy);background:var(--navy);color:#fff;padding:10px 16px;border-radius:10px;font:inherit;font-weight:600;cursor:pointer;transition:.15s}
.btn:hover{background:var(--navy2)}.btn:disabled{opacity:.5}
.btn.prim{background:var(--acc);border-color:var(--acc)}
.btn.ghost{background:transparent;color:var(--navy);border-color:var(--line)}
.btn.sm{padding:6px 12px;font-size:.85rem}.btn.icon{padding:9px;border-radius:10px}
.list{display:flex;flex-direction:column;gap:8px}
.item{display:flex;gap:10px;align-items:flex-start;background:#fff;border:1px solid var(--line);border-radius:12px;padding:12px}
.item.done b{text-decoration:line-through;color:var(--mut)}
.item details{font-size:.8rem;color:var(--mut)}
.chk{width:26px;height:26px;border-radius:8px;border:1.5px solid var(--acc);background:#fff;color:transparent;display:grid;place-items:center;cursor:pointer;flex:none}
.done .chk{background:var(--acc);color:#fff}
.empty{color:var(--mut);text-align:center;padding:24px}
.tabs{display:flex;gap:6px;margin-bottom:12px;flex-wrap:wrap}
.tabs .btn{background:#fff;color:var(--navy);border-color:var(--line)}.tabs .btn.on{background:var(--navy);color:#fff}
.out{background:var(--soft);border-radius:12px;padding:12px;white-space:pre-wrap;min-height:20px}
.out:empty{display:none}
/* chat */
.chatbar{display:flex;gap:8px;margin-bottom:10px}.chatbar select{flex:1}
.msgs{display:flex;flex-direction:column;gap:10px;min-height:46dvh;max-height:58dvh;overflow:auto;padding:4px}
.msg{display:flex}.msg.user{justify-content:flex-end}
.bub{max-width:86%;padding:10px 14px;border-radius:16px;background:#fff;border:1px solid var(--line);word-break:break-word}
.msg.user .bub{background:var(--navy);color:#fff;border-color:var(--navy);border-bottom-right-radius:4px}
.msg.assistant .bub{border-bottom-left-radius:4px}.msg.err .bub{background:#fff1f2;border-color:#fecdd3}
.bub pre{background:#0a1a3a;color:#dbe7ff;padding:10px;border-radius:8px;overflow:auto;margin:6px 0}
.dots i{display:inline-block;width:7px;height:7px;margin:0 2px;border-radius:50%;background:var(--acc);animation:b 1s infinite}
.dots i:nth-child(2){animation-delay:.15s}.dots i:nth-child(3){animation-delay:.3s}
@keyframes b{50%{transform:translateY(-5px);opacity:.4}}
.welcome{margin:auto;text-align:center;color:var(--mut)}
.chips{display:flex;gap:6px;overflow:auto;padding:8px 0}.chips button{white-space:nowrap;border:1px solid var(--line);background:#fff;border-radius:99px;padding:6px 12px;font:inherit;font-size:.82rem;cursor:pointer}
.composer{display:flex;gap:8px;align-items:flex-end}.composer textarea{resize:none;max-height:120px}
/* calendar */
.cal{display:grid;grid-template-columns:repeat(7,1fr);gap:4px;text-align:center}
.cal b{font-size:.75rem;color:var(--mut)}
.cal button{aspect-ratio:1;border:1px solid var(--line);background:#fff;border-radius:10px;font:inherit;cursor:pointer;position:relative}
.cal button.sel{background:var(--navy);color:#fff}.cal button.has::after{content:"";position:absolute;bottom:5px;left:50%;width:5px;height:5px;margin-left:-2.5px;border-radius:50%;background:var(--acc)}
/* bottom nav + sheet */
.bottom{position:fixed;bottom:0;left:0;right:0;display:flex;background:#fff;border-top:1px solid var(--line);padding:6px 6px calc(6px + env(safe-area-inset-bottom));z-index:6}
.bottom a,.bottom button{flex:1;display:flex;flex-direction:column;align-items:center;gap:2px;font-size:.68rem;color:var(--mut);text-decoration:none;background:none;border:0;font-family:inherit;padding:4px}
.bottom .on{color:var(--acc);font-weight:600}
.sheet{position:fixed;inset:0;background:#0a1a3acc;z-index:9;display:flex;align-items:flex-end}
.sheet[hidden]{display:none}
.sheet div{background:#fff;width:100%;border-radius:20px 20px 0 0;padding:14px 12px calc(14px + env(safe-area-inset-bottom));display:grid;grid-template-columns:repeat(2,1fr);gap:4px;animation:up .25s}
.sheet a{color:var(--navy)}
@keyframes up{from{transform:translateY(40px);opacity:0}}
/* voice orb */
.orb{position:fixed;inset:0;z-index:20;background:radial-gradient(circle at 50% 40%,#13306b,#0a1a3a 70%);color:#fff;display:flex;flex-direction:column;align-items:center;justify-content:center;gap:24px;padding:24px;text-align:center;animation:fade .25s}
.orb.idle{display:none}
@keyframes fade{from{opacity:0}}
.wave{display:flex;gap:6px;align-items:center;height:110px;padding:0 26px;border-radius:99px;box-shadow:0 0 calc(14px + var(--lvl)*70px) #3b82f688}
.wave i{width:7px;height:60px;border-radius:5px;background:linear-gradient(#93c5fd,#3b82f6);transform:scaleY(.2);transition:transform .2s}
.orb.listening .wave i,.orb.speaking .wave i{animation:w 1s ease-in-out infinite}
.orb.thinking .wave i{animation:w 1.8s ease-in-out infinite;opacity:.6}
.wave i:nth-child(odd){animation-delay:.12s}.wave i:nth-child(3n){animation-delay:.3s}.wave i:nth-child(4n){animation-delay:.5s}
@keyframes w{50%{transform:scaleY(1)}}
#orbtxt{max-width:520px;font-size:1.1rem;min-height:3em}
#toast{position:fixed;left:50%;bottom:90px;transform:translate(-50%,20px);background:var(--navy);color:#fff;padding:10px 16px;border-radius:12px;opacity:0;pointer-events:none;transition:.25s;z-index:30;max-width:90vw;font-size:.9rem}
#toast.show{opacity:1;transform:translate(-50%,0)}
.auth{margin:auto;max-width:400px;width:100%;padding:20px}
.auth .brand{color:var(--navy);justify-content:center;flex-direction:column;text-align:center;padding-bottom:18px}
.auth .brand img{width:64px;height:64px}.auth .brand small{color:var(--mut)}
@media(min-width:900px){.side{display:flex}.bottom,.mob{display:none!important}.grid{grid-template-columns:repeat(4,1fr)}main{padding-bottom:40px}#toast{bottom:30px}.msgs{max-height:62dvh}}
@media(prefers-reduced-motion:reduce){*{animation:none!important}}
'''

# ───────────────────────── Icons / logo ─────────────────────────
FILES["public/assets/icons.svg"] = r'''<svg xmlns="http://www.w3.org/2000/svg" style="display:none">
<symbol id="home" viewBox="0 0 24 24"><path d="M3 11l9-7 9 7v9a1 1 0 01-1 1h-5v-6H9v6H4a1 1 0 01-1-1z"/></symbol>
<symbol id="chat" viewBox="0 0 24 24"><path d="M4 5h16v11H9l-5 4z"/><path d="M8 9h8M8 12h5"/></symbol>
<symbol id="planner" viewBox="0 0 24 24"><circle cx="12" cy="12" r="4"/><path d="M12 2v3M12 19v3M2 12h3M19 12h3M5 5l2 2M17 17l2 2M19 5l-2 2M7 17l-2 2"/></symbol>
<symbol id="tasks" viewBox="0 0 24 24"><rect x="4" y="3" width="16" height="18" rx="3"/><path d="M8 9l2 2 3-4M8 16h8"/></symbol>
<symbol id="notes" viewBox="0 0 24 24"><path d="M5 3h10l4 4v14H5z"/><path d="M15 3v4h4M8 12h8M8 16h6"/></symbol>
<symbol id="calendar" viewBox="0 0 24 24"><rect x="3" y="5" width="18" height="16" rx="3"/><path d="M3 10h18M8 3v4M16 3v4"/></symbol>
<symbol id="bell" viewBox="0 0 24 24"><path d="M6 17V11a6 6 0 0112 0v6l2 2H4z"/><path d="M10 21h4"/></symbol>
<symbol id="brain" viewBox="0 0 24 24"><path d="M9 4a3 3 0 00-3 3 3 3 0 00-2 5 3 3 0 002 5 3 3 0 006 1V4a3 3 0 00-3 0zM15 4a3 3 0 013 3 3 3 0 012 5 3 3 0 01-2 5 3 3 0 01-6 1"/></symbol>
<symbol id="tools" viewBox="0 0 24 24"><path d="M14 6a4 4 0 005 5l-9 9a2 2 0 01-3-3z"/><path d="M14 6l3-3 4 4-3 3"/></symbol>
<symbol id="file" viewBox="0 0 24 24"><path d="M4 6a2 2 0 012-2h4l2 3h6a2 2 0 012 2v9a2 2 0 01-2 2H6a2 2 0 01-2-2z"/></symbol>
<symbol id="bolt" viewBox="0 0 24 24"><path d="M13 2L5 14h6l-1 8 8-12h-6z"/></symbol>
<symbol id="agent" viewBox="0 0 24 24"><rect x="5" y="8" width="14" height="11" rx="3"/><path d="M12 3v5M9 13h.01M15 13h.01M9 16h6"/></symbol>
<symbol id="settings" viewBox="0 0 24 24"><path d="M4 7h10M18 7h2M4 17h2M10 17h10"/><circle cx="16" cy="7" r="2"/><circle cx="8" cy="17" r="2"/></symbol>
<symbol id="mic" viewBox="0 0 24 24"><rect x="9" y="3" width="6" height="12" rx="3"/><path d="M5 11a7 7 0 0014 0M12 18v3"/></symbol>
<symbol id="clap" viewBox="0 0 24 24"><path d="M3 12c2-3 4-3 5 0M21 12c-2-3-4-3-5 0M8 12l4 7 4-7M12 3v3M6 5l1.5 2M18 5l-1.5 2"/></symbol>
<symbol id="send" viewBox="0 0 24 24"><path d="M4 12l16-8-6 16-3-7z"/></symbol>
<symbol id="plus" viewBox="0 0 24 24"><path d="M12 5v14M5 12h14"/></symbol>
<symbol id="trash" viewBox="0 0 24 24"><path d="M4 7h16M9 7V4h6v3M6 7l1 13h10l1-13"/></symbol>
<symbol id="edit" viewBox="0 0 24 24"><path d="M4 20l1-5L16 4l4 4L9 19z"/></symbol>
<symbol id="logout" viewBox="0 0 24 24"><path d="M9 4H5v16h4M16 8l4 4-4 4M20 12H9"/></symbol>
<symbol id="menu" viewBox="0 0 24 24"><path d="M4 7h16M4 12h16M4 17h16"/></symbol>
<symbol id="check" viewBox="0 0 24 24"><path d="M5 12l5 5 9-10"/></symbol>
</svg>
'''
FILES["public/assets/logo.svg"] = r'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 64 64"><rect width="64" height="64" rx="16" fill="#0a1a3a"/><path d="M14 46V20l18 18 18-18v26" fill="none" stroke="#3b82f6" stroke-width="5" stroke-linecap="round" stroke-linejoin="round"/><circle cx="32" cy="16" r="3.5" fill="#fff"/></svg>
'''
FILES["public/sw.js"] = r'''self.addEventListener('install',()=>self.skipWaiting());
self.addEventListener('activate',e=>e.waitUntil(self.clients.claim()));
self.addEventListener('notificationclick',e=>{e.notification.close();e.waitUntil(clients.openWindow('./'));});
'''

# ───────────────────────── JS ─────────────────────────
FILES["public/js/firebase-config.js"] = r'''// Firebase Console → Project settings → Your apps → Web app → firebaseConfig
// These values are NOT secret (security comes from database.rules.json).
export const firebaseConfig = {
  apiKey: "",
  authDomain: "",
  databaseURL: "",
  projectId: "",
  appId: ""
};
'''

FILES["public/js/core.js"] = r'''import {initializeApp} from "https://www.gstatic.com/firebasejs/10.12.2/firebase-app.js";
import {getAuth,onAuthStateChanged,signInWithEmailAndPassword,createUserWithEmailAndPassword,signOut,GoogleAuthProvider,signInWithPopup} from "https://www.gstatic.com/firebasejs/10.12.2/firebase-auth.js";
import {getDatabase,ref,push,set,update,remove,onValue,get} from "https://www.gstatic.com/firebasejs/10.12.2/firebase-database.js";
import {firebaseConfig} from "./firebase-config.js";

export const configured = !!(firebaseConfig.apiKey && firebaseConfig.databaseURL);
export let auth, db;
if (configured) { const app = initializeApp(firebaseConfig); auth = getAuth(app); db = getDatabase(app); }

export const S = {callName:"Boss", lang:"bn-BD", voiceReply:true, provider:"ollama", endpoint:"http://localhost:11434", model:"llama3.2", sens:5};

export const A = {
  onAuth: cb => onAuthStateChanged(auth, cb),
  login: (e,p) => signInWithEmailAndPassword(auth,e,p),
  signup: (e,p) => createUserWithEmailAndPassword(auth,e,p),
  google: () => signInWithPopup(auth,new GoogleAuthProvider()),
  logout: () => signOut(auth)
};

let uid = null;
export const setUid = u => { uid = u; };
const clean = v => JSON.parse(JSON.stringify(v));
const p = path => ref(db, `users/${uid}/${path}`);
export const D = {
  add: async (path,val) => { const r = push(p(path)); await set(r, clean({...val, createdAt: Date.now()})); return r.key; },
  put: (path,val) => set(p(path), clean(val)),
  patch: (path,val) => update(p(path), clean(val)),
  del: path => remove(p(path)),
  get: async path => (await get(p(path))).val(),
  watch: (path,cb,err) => onValue(p(path), s => cb(s.val()), err),
  all: async () => (await get(ref(db, `users/${uid}`))).val(),
  wipe: () => remove(ref(db, `users/${uid}`))
};
'''

FILES["public/js/ai.js"] = r'''import {S, auth} from "./core.js";
export const isBn = t => /[\u0980-\u09FF]/.test(t || "");

// Providers (no paid API required):
//  ollama : local model on your own device/PC (free, private)
//  proxy  : your own free Cloudflare Worker (worker/worker.js) which keeps the secret key server-side
export async function ask(messages, memory = [], opt = {}) {
  const sys = opt.sys || `You are Mayra, a personal AI assistant. Address the user as "${S.callName}". Reply in the same language as the user's last message (Bengali or English). Be concise and honest. Never claim you performed an action (saving, scheduling, sending) unless the app confirmed it.` +
    (memory.length ? `\nFacts the user asked you to remember:\n- ${memory.join("\n- ")}` : "");
  const msgs = [{role:"system", content:sys}, ...messages];
  const base = (S.endpoint || "").replace(/\/$/, "");
  if (!base) throw new Error("AI endpoint সেট করা নেই");
  if (S.provider === "ollama") {
    const r = await fetch(base + "/api/chat", {method:"POST", headers:{"Content-Type":"application/json"}, body:JSON.stringify({model:S.model, messages:msgs, stream:false})});
    if (!r.ok) throw new Error("Ollama HTTP " + r.status);
    const j = await r.json(); return j.message?.content || "";
  }
  const token = await auth.currentUser.getIdToken();
  const r = await fetch(S.endpoint, {method:"POST", headers:{"Content-Type":"application/json", Authorization:"Bearer " + token}, body:JSON.stringify({model:S.model || undefined, messages:msgs})});
  if (!r.ok) throw new Error("Proxy HTTP " + r.status);
  const j = await r.json(); return j.choices?.[0]?.message?.content || "";
}

export async function listModels() {
  if (S.provider !== "ollama") throw new Error("Model তালিকা শুধু Ollama-তে পাওয়া যায়");
  const r = await fetch(S.endpoint.replace(/\/$/, "") + "/api/tags");
  if (!r.ok) throw new Error("HTTP " + r.status);
  return ((await r.json()).models || []).map(m => m.name);
}
'''

FILES["public/js/voice.js"] = r'''import {S} from "./core.js";
import {isBn} from "./ai.js";
const SR = window.SpeechRecognition || window.webkitSpeechRecognition;
export const supported = {sr: !!SR, tts: "speechSynthesis" in window};

export function speak(text) {
  return new Promise(res => {
    if (!supported.tts || !S.voiceReply) return res();
    speechSynthesis.cancel();
    const u = new SpeechSynthesisUtterance(String(text).replace(/[*_`#]/g, ""));
    u.lang = isBn(text) ? "bn-BD" : "en-US";
    const v = speechSynthesis.getVoices().find(v => v.lang.replace("_", "-").toLowerCase().startsWith(u.lang.slice(0, 2)));
    if (v) u.voice = v;
    u.onend = u.onerror = () => res();
    speechSynthesis.speak(u);
  });
}

let cur = null;
export const stopListen = () => { try { cur && cur.abort(); } catch {} };
export function listen(lang) {
  return new Promise((res, rej) => {
    if (!SR) return rej(new Error("এই ব্রাউজারে Speech Recognition নেই (Chrome ব্যবহার করুন)"));
    const r = new SR(); cur = r;
    r.lang = lang || S.lang || "bn-BD"; r.interimResults = false; r.maxAlternatives = 1;
    r.onresult = e => res(e.results[0][0].transcript);
    r.onerror = e => e.error === "no-speech" || e.error === "aborted" ? res("") : rej(new Error(e.error));
    r.onend = () => res("");
    r.start();
  });
}

// Clap detection: the microphone is read live in memory only. Nothing is recorded, saved or uploaded.
let ctx, stream, raf, on = false, paused = false, avg = 0, last = 0;
export const setPaused = v => { paused = v; };
export async function startClap(onClap, onLevel) {
  stream = await navigator.mediaDevices.getUserMedia({audio:{echoCancellation:false, noiseSuppression:false, autoGainControl:false}});
  ctx = new AudioContext(); await ctx.resume();
  const an = ctx.createAnalyser(); an.fftSize = 1024;
  ctx.createMediaStreamSource(stream).connect(an);
  const buf = new Float32Array(an.fftSize); on = true;
  const tick = () => {
    if (!on) return;
    an.getFloatTimeDomainData(buf);
    let s = 0, pk = 0;
    for (const x of buf) { s += x * x; pk = Math.max(pk, Math.abs(x)); }
    const rms = Math.sqrt(s / buf.length);
    onLevel && onLevel(rms);
    const th = 0.55 - S.sens * 0.045;                 // sensitivity 1..10
    const now = performance.now();
    if (!paused && pk > th && rms > avg * 3 + 0.01 && now - last > 1500) { last = now; onClap(); }
    avg = avg * 0.95 + rms * 0.05;
    raf = requestAnimationFrame(tick);
  };
  tick();
}
export function stopClap() {
  on = false; cancelAnimationFrame(raf);
  stream && stream.getTracks().forEach(t => t.stop());
  ctx && ctx.close();
}
'''

FILES["public/js/app.js"] = r'''import {configured, A, D, S, setUid} from "./core.js";
import {ask, isBn, listModels} from "./ai.js";
import {speak, listen, stopListen, startClap, stopClap, setPaused, supported} from "./voice.js";

const $ = (s, r = document) => r.querySelector(s);
const pad = n => String(n).padStart(2, "0");
const esc = s => String(s ?? "").replace(/[&<>"']/g, c => ({"&":"&amp;","<":"&lt;",">":"&gt;",'"':"&quot;","'":"&#39;"}[c]));
const md = s => esc(s).replace(/```([\s\S]*?)```/g, "<pre>$1</pre>").replace(/\*\*(.+?)\*\*/g, "<b>$1</b>").replace(/`([^`]+)`/g, "<code>$1</code>").replace(/\n/g, "<br>");
const ic = n => `<svg class="i"><use href="assets/icons.svg#${n}"/></svg>`;
const ymd = d => `${d.getFullYear()}-${pad(d.getMonth() + 1)}-${pad(d.getDate())}`;
const toLocal = d => `${ymd(d)}T${pad(d.getHours())}:${pad(d.getMinutes())}`;
const fmt = t => t ? new Date(t).toLocaleString() : "";
const toast = (m, t = 3500) => { const e = $("#toast"); e.textContent = m; e.className = "show"; clearTimeout(toast.t); toast.t = setTimeout(() => e.className = "", t); };

const NAMES = ["tasks","notes","reminders","memory","automations","agents","files","chats"];
const C = {}; NAMES.forEach(n => C[n] = {});
const list = n => Object.entries(C[n] || {}).map(([id, v]) => ({id, ...v})).sort((a, b) => (b.createdAt || 0) - (a.createdAt || 0));
let onData = () => {}, subs = [], view = "", clapOn = false, booted = false;
const chat = {id: null, msgs: [], busy: false};

/* ───────── boot / auth ───────── */
if ("serviceWorker" in navigator) navigator.serviceWorker.register("sw.js").catch(() => {});
if (!configured) renderSetup(); else A.onAuth(async u => {
  if (!u) { teardown(); return renderAuth(); }
  setUid(u.uid);
  try {
    if (!(await D.get("profile"))) await D.put("profile", {email: u.email || "", name: u.displayName || "", createdAt: Date.now()});
    Object.assign(S, (await D.get("settings")) || {});
  } catch (e) { toast("Database error: " + e.message, 8000); }
  NAMES.forEach(n => subs.push(D.watch(n, v => { C[n] = v || {}; onData(); }, e => toast(n + ": " + e.message))));
  renderShell(); startEngines();
  go(location.hash.slice(1) || "dashboard");
});
function teardown() { subs.forEach(f => f && f()); subs = []; NAMES.forEach(n => C[n] = {}); if (clapOn) { stopClap(); clapOn = false; } chat.id = null; chat.msgs = []; }

function renderSetup() {
  $("#app").innerHTML = `<div class="auth"><div class="brand"><img src="assets/logo.svg" alt=""><b>MAYRA</b></div><div class="card"><h3>Firebase সেটআপ বাকি</h3><p>public/js/firebase-config.js ফাইলে আপনার Firebase web config বসান, তারপর আবার deploy করুন। বিস্তারিত README.md-তে আছে।</p></div></div>`;
}
function renderAuth() {
  let mode = "login";
  const draw = () => {
    $("#app").innerHTML = `<div class="auth"><div class="brand"><img src="assets/logo.svg" alt=""><b>MAYRA</b><small>Your Personal AI Assistant</small></div>
    <form id="af" class="card"><label>Email<input name="e" type="email" required autocomplete="email"></label>
    <label>Password<input name="p" type="password" minlength="6" required autocomplete="${mode === "login" ? "current-password" : "new-password"}"></label>
    <button class="btn">${mode === "login" ? "লগইন · Sign in" : "অ্যাকাউন্ট খুলুন · Sign up"}</button>
    <button type="button" id="g" class="btn ghost">Google দিয়ে চালিয়ে যান</button>
    <button type="button" id="sw" class="btn ghost">${mode === "login" ? "নতুন? Sign up" : "আছে? Sign in"}</button></form></div>`;
    $("#sw").onclick = () => { mode = mode === "login" ? "signup" : "login"; draw(); };
    $("#g").onclick = () => A.google().catch(e => toast(e.message));
    $("#af").onsubmit = e => { e.preventDefault(); const f = e.target; (mode === "login" ? A.login : A.signup)(f.e.value, f.p.value).catch(x => toast(x.message, 6000)); };
  };
  draw();
}

/* ───────── shell / routing ───────── */
const NAV = [["dashboard","home","হোম · Home"],["chat","chat","চ্যাট · Chat"],["planner","planner","প্ল্যানার · Planner"],["tasks","tasks","টাস্ক · Tasks"],["notes","notes","নোট · Notes"],["calendar","calendar","ক্যালেন্ডার · Calendar"],["reminders","bell","রিমাইন্ডার · Reminders"],["memory","brain","মেমরি · Memory"],["tools","tools","টুলস · Tools"],["files","file","ফাইল/PDF · Files"],["automations","bolt","অটোমেশন · Automations"],["agents","agent","এজেন্ট · Agents"],["settings","settings","সেটিংস · Settings"]];
function renderShell() {
  if (booted) return; booted = true;
  const link = ([k, i, l]) => `<a href="#${k}" data-v="${k}">${ic(i)}<span>${l}</span></a>`;
  $("#app").innerHTML = `<aside class="side"><div class="brand"><img src="assets/logo.svg" alt=""><div><b>MAYRA</b><small>Your Personal AI Assistant</small></div></div><nav>${NAV.map(link).join("")}</nav><button id="out" class="navbtn">${ic("logout")}<span>লগআউট</span></button></aside>
  <div class="content"><header class="top"><button id="menu" class="btn icon ghost mob" aria-label="menu">${ic("menu")}</button><span class="mic" id="micb">মাইক বন্ধ</span><span class="grow"></span><button id="orbbtn" class="btn icon prim" aria-label="voice">${ic("mic")}</button></header><main id="main"></main></div>
  <nav class="bottom">${NAV.filter(n => ["dashboard","chat","tasks","planner"].includes(n[0])).map(link).join("")}<button id="more">${ic("menu")}<span>আরও</span></button></nav>
  <div id="sheet" class="sheet" hidden><div>${NAV.map(link).join("")}<a href="#" id="out2">${ic("logout")}<span>লগআউট</span></a></div></div>
  <div id="orb" class="orb idle"><div class="wave">${"<i></i>".repeat(11)}</div><p id="orbtxt"></p><button id="orbstop" class="btn">বন্ধ · Stop</button></div>`;
  $("#menu").onclick = $("#more").onclick = () => $("#sheet").hidden = false;
  $("#sheet").onclick = e => { if (e.target.closest("a,#sheet")) $("#sheet").hidden = true; };
  $("#out").onclick = () => { booted = false; A.logout(); };
  $("#out2").onclick = e => { e.preventDefault(); booted = false; A.logout(); };
  $("#orbbtn").onclick = () => voiceTurn(false);
  $("#orbstop").onclick = () => { stopListen(); speechSynthesis.cancel(); setOrb("idle"); };
  window.onhashchange = () => go(location.hash.slice(1));
}
function go(v) {
  if (!views[v]) v = "dashboard";
  view = v; onData = () => {}; $("#main").innerHTML = "";
  document.querySelectorAll("[data-v]").forEach(a => a.classList.toggle("on", a.dataset.v === v));
  views[v](); scrollTo(0, 0);
}
function setOrb(state, txt = "") { const o = $("#orb"); if (!o) return; o.className = "orb " + state; $("#orbtxt").textContent = txt; }
function setBadge() { const b = $("#micb"); if (!b) return; b.className = "mic" + (clapOn ? " on" : ""); b.textContent = clapOn ? "মাইক চালু · Clap শোনা হচ্ছে" : "মাইক বন্ধ"; const l = $("#claplbl"); if (l) l.textContent = clapOn ? "Clap to Wake বন্ধ করুন" : "Clap to Wake চালু করুন"; }

/* ───────── generic CRUD ───────── */
const fieldHtml = q => `<label>${q.l}${q.t === "textarea" ? `<textarea name="${q.k}" rows="3" ${q.req ? "required" : ""}></textarea>` : q.t === "select" ? `<select name="${q.k}">${q.o.map(o => `<option>${o}</option>`).join("")}</select>` : q.t === "check" ? `<input type="checkbox" name="${q.k}">` : `<input name="${q.k}" type="${q.t || "text"}" ${q.a || ""} ${q.req ? "required" : ""}>`}</label>`;
const getField = (f, q) => { const el = f.elements[q.k]; return q.t === "check" ? el.checked : q.t === "number" || q.t === "range" ? Number(el.value) || 0 : el.value; };
const setField = (f, q, v) => { const el = f.elements[q.k]; if (q.t === "check") el.checked = !!v; else el.value = v ?? q.d ?? ""; };

const hist = x => { const h = Object.values(x.history || {}).sort((a, b) => b.at - a.at).slice(0, 3); return h.length ? `<details><summary>History (${h.length})</summary>${h.map(e => `${fmt(e.at)} — <b>${esc(e.status)}</b>${(e.log || []).map(l => `<br>• ${esc(l.step)}: ${esc(l.status)} (${esc(l.detail)})`).join("")}`).join("<hr>")}</details>` : ""; };
const DEF = {
  tasks: {title: "টাস্ক · Tasks", done: 1, f: [{k:"title",l:"শিরোনাম",req:1},{k:"due",l:"তারিখ",t:"date"},{k:"priority",l:"গুরুত্ব",t:"select",o:["low","medium","high"],d:"medium"},{k:"details",l:"বিবরণ",t:"textarea"}], sum: x => esc(`${x.due || ""} ${x.priority || ""}`)},
  notes: {title: "নোট · Notes", f: [{k:"title",l:"শিরোনাম",req:1},{k:"body",l:"লেখা",t:"textarea"}], sum: x => esc((x.body || "").slice(0, 160))},
  reminders: {title: "রিমাইন্ডার · Reminders", done: 1, f: [{k:"title",l:"কী মনে করাবো",req:1},{k:"at",l:"কখন",t:"datetime-local",req:1},{k:"repeat",l:"পুনরাবৃত্তি",t:"select",o:["none","daily","weekly"]}], sum: x => esc(`${(x.at || "").replace("T", " ")} · ${x.repeat || "none"}`)},
  memory: {title: "পার্সোনাল মেমরি · Memory", f: [{k:"text",l:"Mayra যা মনে রাখবে",t:"textarea",req:1}], sum: () => "AI chat-এ প্রসঙ্গ হিসেবে যায়"},
  agents: {title: "এজেন্ট · AI Agents", f: [{k:"name",l:"নাম",req:1},{k:"instructions",l:"নির্দেশনা (system prompt)",t:"textarea",req:1}], sum: x => esc((x.instructions || "").slice(0, 100)),
    extra: () => `<div class="row"><input placeholder="কাজ দিন…"><button class="btn sm" data-a="run">চালান</button></div><div class="out"></div>`,
    act: async (a, id, x, b) => { if (a !== "run") return; const q = b.parentElement.querySelector("input").value.trim(), out = b.closest(".item").querySelector(".out"); if (!q) return; b.disabled = true; out.textContent = "…"; try { out.innerHTML = md(await ask([{role:"user", content:q}], [], {sys:x.instructions})); } catch (e) { out.textContent = "ত্রুটি: " + e.message; } b.disabled = false; }},
  automations: {title: "অটোমেশন · Automations", f: [{k:"name",l:"নাম",req:1},{k:"enabled",l:"চালু",t:"check"},{k:"trigger",l:"ট্রিগার",t:"select",o:["interval","daily"]},{k:"every",l:"interval: কত মিনিট পরপর",t:"number",a:'min="1"'},{k:"at",l:"daily: সময়",t:"time"},{k:"cond",l:"শর্ত",t:"select",o:["always","tasks_gt","weekday"]},{k:"condN",l:"tasks_gt: pending টাস্ক এর বেশি হলে (সংখ্যা)",t:"number"},{k:"steps",l:"ধাপ (প্রতি লাইনে একটি): notify: … | task: … | note: … | ai: … | speak: …",t:"textarea",req:1}],
    extra: x => `<small>${x.trigger === "daily" ? "প্রতিদিন " + esc(x.at) : "প্রতি " + esc(x.every) + " মিনিট"} · শর্ত: ${esc(x.cond || "always")} · ${x.enabled ? "চালু" : "বন্ধ"}</small><small>সর্বশেষ: ${x.lastStatus ? esc(x.lastStatus) + " · " + fmt(x.lastRun) : "এখনো চলেনি"}</small>${hist(x)}<button class="btn sm" data-a="run">এখনই চালান</button>`,
    act: async (a, id, x, b) => { if (a !== "run") return; b.disabled = true; await runAuto(id, true); toast("চালানো শেষ — History দেখুন"); b.disabled = false; }}
};
function crud(n) {
  const d = DEF[n]; let edit = null;
  $("#main").innerHTML = `<h1>${d.title}</h1><form id="f" class="card">${d.f.map(fieldHtml).join("")}<div class="row"><button class="btn prim">${ic("check")} সেভ · Save</button><button type="button" id="cancel" class="btn ghost" hidden>বাতিল</button></div></form><div id="list" class="list"></div>`;
  const f = $("#f"), reset = () => { f.reset(); edit = null; $("#cancel").hidden = true; };
  const draw = () => { const items = list(n); $("#list").innerHTML = items.length ? items.map(x => `<div class="item ${x.done ? "done" : ""}" data-id="${x.id}">${d.done ? `<button class="chk" data-a="tog" aria-label="done">${ic("check")}</button>` : ""}<div class="grow"><b>${esc(x[d.f[0].k])}</b><small>${d.sum ? d.sum(x) : ""}</small>${d.extra ? d.extra(x) : ""}</div><button class="btn icon ghost" data-a="edit" aria-label="edit">${ic("edit")}</button><button class="btn icon ghost" data-a="del" aria-label="delete">${ic("trash")}</button></div>`).join("") : `<p class="empty">এখনো কিছু নেই · Nothing yet</p>`; };
  onData = draw; draw();
  $("#cancel").onclick = reset;
  $("#list").onclick = async e => {
    const b = e.target.closest("[data-a]"); if (!b) return;
    const id = b.closest(".item").dataset.id, x = C[n][id], a = b.dataset.a;
    try {
      if (a === "del") { if (confirm("মুছবেন? Delete?")) await D.del(`${n}/${id}`); }
      else if (a === "tog") await D.patch(`${n}/${id}`, {done: !x.done});
      else if (a === "edit") { edit = id; d.f.forEach(q => setField(f, q, x[q.k])); $("#cancel").hidden = false; scrollTo(0, 0); }
      else if (d.act) await d.act(a, id, x, b);
    } catch (err) { toast("ত্রুটি: " + err.message, 6000); }
  };
  f.onsubmit = async e => {
    e.preventDefault(); const v = {}; d.f.forEach(q => v[q.k] = getField(f, q));
    try { if (edit) await D.patch(`${n}/${edit}`, v); else await D.add(n, {...v, done: false}); toast("সেভ হয়েছে (সার্ভারে নিশ্চিত)"); reset(); } catch (err) { toast("সেভ হয়নি: " + err.message, 6000); }
  };
}

/* ───────── chat engine ───────── */
const greeting = () => S.lang === "en-US" ? `Yes, ${S.callName}. How can I help you?` : `জি ${S.callName}, বলুন! আমি শুনছি।`;
function renderMsgs() {
  const el = $("#msgs"); if (!el) return;
  el.innerHTML = (chat.msgs.length ? chat.msgs.map(m => `<div class="msg ${m.role}${m.error ? " err" : ""}"><div class="bub">${md(m.content)}</div></div>`).join("") : `<div class="welcome"><b>${esc(S.callName)}</b>, কীভাবে সাহায্য করতে পারি?<br>How can I help?</div>`) + (chat.busy ? `<div class="msg assistant"><div class="bub dots"><i></i><i></i><i></i></div></div>` : "");
  el.scrollTop = el.scrollHeight;
}
async function send(text, voice) {
  if (chat.busy) return;
  if (!chat.id) { chat.id = await D.add("chats", {title: text.slice(0, 40), updatedAt: Date.now()}); chat.msgs = []; }
  const um = {role: "user", content: text, ts: Date.now()};
  chat.msgs.push(um); chat.busy = true; renderMsgs();
  D.add(`chatMessages/${chat.id}`, um).catch(e => toast("সেভ হয়নি: " + e.message));
  let reply = null, err = "";
  const mm = text.match(/^\s*(?:remember|মনে রাখো|মনে রাখ)\s*[:,\-]?\s*([\s\S]+)$/i);
  try {
    if (mm) {
      const k = await D.add("memory", {text: mm[1].trim()});
      if (!(await D.get("memory/" + k))) throw new Error("যাচাই ব্যর্থ");
      reply = isBn(text) ? `ঠিক আছে ${S.callName}, মনে রাখলাম: ${mm[1].trim()}` : `Saved to memory, ${S.callName}: ${mm[1].trim()}`;
    } else reply = await ask(chat.msgs.filter(m => !m.error).slice(-14).map(({role, content}) => ({role, content})), list("memory").map(m => m.text));
  } catch (e) { err = e.message; }
  chat.busy = false;
  const am = reply ? {role: "assistant", content: reply, ts: Date.now()} : {role: "assistant", error: true, content: `AI থেকে উত্তর আনা যায়নি: ${err}\nSettings → AI অংশ দেখুন।`, ts: Date.now()};
  chat.msgs.push(am); renderMsgs();
  if (reply) D.add(`chatMessages/${chat.id}`, am).catch(() => {});
  D.patch(`chats/${chat.id}`, {updatedAt: Date.now()}).catch(() => {});
  if (voice && reply) { setOrb("speaking", reply.slice(0, 160)); await speak(reply); }
}
async function loadChat(id) { chat.id = id || null; chat.msgs = id ? Object.values((await D.get("chatMessages/" + id)) || {}).sort((a, b) => a.ts - b.ts) : []; renderMsgs(); }

async function voiceTurn(greet) {
  if (view !== "chat") go("chat");
  try {
    if (greet) { setOrb("speaking", greeting()); await speak(greeting()); }
    setOrb("listening", "শুনছি… · Listening…");
    const t = await listen(S.lang);
    if (!t) { toast("কিছু শোনা যায়নি"); return; }
    setOrb("thinking", t); await send(t, true);
  } catch (e) { toast("Voice: " + e.message, 6000); } finally { setOrb("idle"); }
}
async function onClap() { setPaused(true); try { await voiceTurn(true); } finally { setPaused(false); } }
async function toggleClap() {
  if (clapOn) { stopClap(); clapOn = false; setBadge(); return toast("Clap listening বন্ধ"); }
  try { await startClap(onClap, l => document.documentElement.style.setProperty("--lvl", Math.min(1, l * 6))); clapOn = true; setBadge(); toast("মাইক চালু। ট্যাব খোলা ও স্ক্রিন অন রাখুন।", 6000); }
  catch (e) { toast("মাইক অনুমতি পাওয়া যায়নি: " + e.message, 6000); }
}

/* ───────── notifications / engines ───────── */
async function notify(title, body) {
  toast(body, 6000);
  const reg = "serviceWorker" in navigator ? await navigator.serviceWorker.getRegistration() : null;
  if (reg && "Notification" in window && Notification.permission === "granted") { await reg.showNotification(title, {body, icon: "assets/logo.svg"}); return "সিস্টেম নোটিফিকেশন পাঠানো হয়েছে"; }
  return "শুধু অ্যাপের ভেতরে বার্তা দেখানো হয়েছে (নোটিফিকেশন অনুমতি নেই)";
}
async function checkReminders() {
  const now = Date.now();
  for (const r of list("reminders")) {
    if (r.done || !r.at || r.firedFor === r.at || new Date(r.at).getTime() > now) continue;
    try {
      await D.patch(`reminders/${r.id}`, {firedFor: r.at});
      await notify("রিমাইন্ডার", r.title); speak(`${S.callName}, ${r.title}`);
      if (r.repeat && r.repeat !== "none") { const nt = new Date(r.at); do nt.setDate(nt.getDate() + (r.repeat === "daily" ? 1 : 7)); while (nt.getTime() <= now); await D.patch(`reminders/${r.id}`, {at: toLocal(nt)}); }
    } catch (e) { toast("Reminder error: " + e.message); }
  }
}
const verify = async path => { if (!(await D.get(path))) throw new Error("লিখে যাচাই করা যায়নি"); };
async function runAuto(id, manual) {
  const a = C.automations[id]; if (!a) return;
  const log = []; let status = "success";
  const pend = list("tasks").filter(t => !t.done).length;
  const skip = (a.cond === "tasks_gt" && !(pend > (+a.condN || 0))) || (a.cond === "weekday" && [0, 6].includes(new Date().getDay()));
  if (skip) { status = "skipped"; log.push({step: "শর্ত", status: "skipped", detail: "শর্ত পূরণ হয়নি"}); }
  else for (const line of String(a.steps || "").split("\n").map(s => s.trim()).filter(Boolean)) {
    const m = line.match(/^(notify|task|note|ai|speak)\s*:\s*([\s\S]+)$/i);
    if (!m) { log.push({step: line, status: "error", detail: "অজানা ধাপ"}); status = "failed"; break; }
    const k = m[1].toLowerCase(), arg = m[2];
    try {
      let detail = "";
      if (k === "notify") detail = await notify("Mayra", arg);
      else if (k === "task") { const t = await D.add("tasks", {title: arg, done: false, priority: "medium", due: ymd(new Date()), by: "automation"}); await verify("tasks/" + t); detail = "টাস্ক তৈরি ও যাচাই হয়েছে"; }
      else if (k === "note") { const t = await D.add("notes", {title: arg.slice(0, 40), body: arg, by: "automation"}); await verify("notes/" + t); detail = "নোট তৈরি ও যাচাই হয়েছে"; }
      else if (k === "ai") { const r = await ask([{role: "user", content: arg}], []); if (!r) throw new Error("খালি উত্তর"); const t = await D.add("notes", {title: "AI: " + arg.slice(0, 40), body: r, by: "automation"}); await verify("notes/" + t); detail = "AI উত্তর নোটে সেভ ও যাচাই হয়েছে"; }
      else { await speak(arg); detail = "Speech চালানো হয়েছে (শোনা গেছে কিনা যাচাই সম্ভব নয়)"; }
      log.push({step: line, status: "ok", detail});
    } catch (e) { log.push({step: line, status: "error", detail: e.message}); status = "failed"; break; }
  }
  try { await D.add(`automations/${id}/history`, {at: Date.now(), status, log, manual: !!manual}); await D.patch(`automations/${id}`, {lastRun: Date.now(), lastDay: ymd(new Date()), lastStatus: status}); } catch (e) { toast("History সেভ হয়নি: " + e.message); }
}
let engineOn = false; const running = {};
function startEngines() {
  if (engineOn) return; engineOn = true;
  setInterval(() => {
    const now = Date.now(), d = new Date(), hm = `${pad(d.getHours())}:${pad(d.getMinutes())}`;
    for (const a of list("automations")) {
      if (!a.enabled || running[a.id]) continue;
      const due = a.trigger === "daily" ? a.at === hm && a.lastDay !== ymd(d) : now - (a.lastRun || a.createdAt || now) >= Math.max(1, +a.every || 60) * 60000;
      if (due) { running[a.id] = 1; runAuto(a.id).finally(() => delete running[a.id]); }
    }
    checkReminders();
  }, 20000);
}

/* ───────── views ───────── */
const views = {};
views.dashboard = () => {
  const draw = () => {
    const t = list("tasks").filter(x => !x.done), td = ymd(new Date());
    const r = list("reminders").filter(x => !x.done && (x.at || "").startsWith(td));
    const h = new Date().getHours();
    $("#main").innerHTML = `<h1>${h < 12 ? "সুপ্রভাত" : h < 18 ? "শুভ অপরাহ্ন" : "শুভ সন্ধ্যা"}, ${esc(S.callName)}</h1><p class="sub">Your Personal AI Assistant</p>
    <div class="row"><button id="talk" class="btn prim">${ic("mic")} Mayra-র সাথে কথা বলুন</button><button id="clap" class="btn ghost">${ic("clap")} <span id="claplbl"></span></button></div>
    <div class="grid"><div class="stat"><b>${t.length}</b><span>পেন্ডিং টাস্ক</span></div><div class="stat"><b>${r.length}</b><span>আজকের রিমাইন্ডার</span></div><div class="stat"><b>${list("notes").length}</b><span>নোট</span></div><div class="stat"><b>${list("automations").filter(a => a.enabled).length}</b><span>চালু অটোমেশন</span></div></div>
    <div class="card"><h3>আজকের এজেন্ডা</h3>${[...t.filter(x => !x.due || x.due <= td).slice(0, 6).map(x => `<div>• ${esc(x.title)}</div>`), ...r.map(x => `<div>• ${esc((x.at || "").slice(11))} ${esc(x.title)}</div>`)].join("") || '<p class="empty">আজ কিছু নেই</p>'}</div>`;
    $("#talk").onclick = () => voiceTurn(true); $("#clap").onclick = toggleClap; setBadge();
  };
  onData = draw; draw();
};

views.chat = () => {
  $("#main").innerHTML = `<div class="chatbar"><select id="csel"></select><button id="cnew" class="btn sm">${ic("plus")} নতুন</button><button id="cdel" class="btn sm ghost" aria-label="delete chat">${ic("trash")}</button></div><div id="msgs" class="msgs"></div>
  <div class="chips">${["আজকের কাজের প্ল্যান সাজাও","Summarize my day","Remember: ","এটা ইংরেজিতে অনুবাদ করো: "].map(c => `<button type="button">${esc(c)}</button>`).join("")}</div>
  <form id="cf" class="composer"><textarea id="ci" rows="1" placeholder="Mayra-কে লিখুন… / Message Mayra…"></textarea><button type="button" id="cmic" class="btn icon ghost" aria-label="voice">${ic("mic")}</button><button class="btn icon prim" aria-label="send">${ic("send")}</button></form>`;
  const sel = $("#csel");
  const fill = () => { const cs = list("chats").sort((a, b) => (b.updatedAt || 0) - (a.updatedAt || 0)); sel.innerHTML = `<option value="">— নতুন চ্যাট —</option>` + cs.map(c => `<option value="${c.id}" ${c.id === chat.id ? "selected" : ""}>${esc(c.title)}</option>`).join(""); };
  onData = fill; fill(); renderMsgs();
  sel.onchange = () => loadChat(sel.value);
  $("#cnew").onclick = () => { loadChat(null); sel.value = ""; };
  $("#cdel").onclick = async () => { if (!chat.id || !confirm("এই চ্যাট মুছবেন?")) return; const id = chat.id; await D.del("chats/" + id); await D.del("chatMessages/" + id); loadChat(null); };
  document.querySelectorAll(".chips button").forEach(b => b.onclick = () => { $("#ci").value = b.textContent; $("#ci").focus(); });
  $("#cmic").onclick = () => voiceTurn(false);
  const sub = () => { const t = $("#ci").value.trim(); if (!t) return; $("#ci").value = ""; send(t); };
  $("#cf").onsubmit = e => { e.preventDefault(); sub(); };
  $("#ci").onkeydown = e => { if (e.key === "Enter" && !e.shiftKey) { e.preventDefault(); sub(); } };
};

views.planner = () => {
  $("#main").innerHTML = `<h1>ডেইলি প্ল্যানার</h1><div class="card" id="ag"></div><button id="pl" class="btn prim">${ic("planner")} AI দিয়ে আজকের প্ল্যান বানান</button><div class="out" id="po"></div><button id="ps" class="btn ghost" hidden>নোট হিসেবে সেভ</button>`;
  const td = () => ymd(new Date()), ctx = () => ({t: list("tasks").filter(x => !x.done && (!x.due || x.due <= td())), r: list("reminders").filter(x => !x.done && (x.at || "").startsWith(td()))});
  const draw = () => { const {t, r} = ctx(); $("#ag").innerHTML = `<h3>আজ · ${td()}</h3>` + ([...t.map(x => `<div>☐ ${esc(x.title)} <small>${esc(x.priority || "")}</small></div>`), ...r.map(x => `<div>${esc((x.at || "").slice(11))} — ${esc(x.title)}</div>`)].join("") || '<p class="empty">কিছু নেই</p>'); };
  onData = draw; draw(); let plan = "";
  $("#pl").onclick = async e => {
    const {t, r} = ctx(); e.target.disabled = true; $("#po").textContent = "…";
    try { plan = await ask([{role: "user", content: `Today is ${td()}. Pending tasks:\n${t.map(x => `- ${x.title} (${x.priority})`).join("\n") || "none"}\nReminders today:\n${r.map(x => `- ${x.at} ${x.title}`).join("\n") || "none"}\nCreate a realistic time-blocked plan for today. Reply in ${S.lang === "en-US" ? "English" : "Bengali"}.`}], list("memory").map(m => m.text)); $("#po").innerHTML = md(plan); $("#ps").hidden = false; }
    catch (err) { $("#po").textContent = "ত্রুটি: " + err.message; }
    e.target.disabled = false;
  };
  $("#ps").onclick = async () => { await D.add("notes", {title: "প্ল্যান " + td(), body: plan}); toast("নোটে সেভ হয়েছে"); };
};

views.calendar = () => {
  let m = new Date(); m.setDate(1); let sel = ymd(new Date());
  const ev = d => [...list("tasks").filter(t => t.due === d).map(t => ({k: "টাস্ক", x: t.title, done: t.done})), ...list("reminders").filter(r => (r.at || "").startsWith(d)).map(r => ({k: "রিমাইন্ডার", x: (r.at || "").slice(11) + " " + r.title, done: r.done}))];
  const draw = () => {
    const y = m.getFullYear(), mo = m.getMonth(), first = m.getDay(), days = new Date(y, mo + 1, 0).getDate();
    let cells = "<b>র</b><b>সো</b><b>ম</b><b>বু</b><b>বৃ</b><b>শু</b><b>শ</b>" + "<span></span>".repeat(first);
    for (let d = 1; d <= days; d++) { const k = `${y}-${pad(mo + 1)}-${pad(d)}`; cells += `<button data-d="${k}" class="${k === sel ? "sel" : ""} ${ev(k).length ? "has" : ""}">${d}</button>`; }
    $("#main").innerHTML = `<h1>ক্যালেন্ডার</h1><div class="row card" style="flex-direction:row"><button id="pv" class="btn sm ghost">‹</button><b class="grow" style="text-align:center">${m.toLocaleString("bn-BD", {month: "long", year: "numeric"})}</b><button id="nx" class="btn sm ghost">›</button></div><div class="cal">${cells}</div>
    <div class="card" style="margin-top:12px"><h3>${sel}</h3>${ev(sel).map(e => `<div>• <small style="display:inline">${e.k}</small> ${esc(e.x)}</div>`).join("") || '<p class="empty">কিছু নেই</p>'}<div class="row"><input id="qt" placeholder="এই দিনে নতুন টাস্ক…" style="flex:1"><button id="qa" class="btn sm">${ic("plus")}</button></div></div>`;
    $("#pv").onclick = () => { m.setMonth(m.getMonth() - 1); draw(); }; $("#nx").onclick = () => { m.setMonth(m.getMonth() + 1); draw(); };
    document.querySelectorAll(".cal [data-d]").forEach(b => b.onclick = () => { sel = b.dataset.d; draw(); });
    $("#qa").onclick = async () => { const t = $("#qt").value.trim(); if (!t) return; try { await D.add("tasks", {title: t, due: sel, priority: "medium", done: false}); toast("টাস্ক যোগ হয়েছে"); } catch (e) { toast(e.message); } };
  };
  onData = () => { if (document.activeElement?.id !== "qt") draw(); }; draw();
};

views.tasks = () => crud("tasks"); views.notes = () => crud("notes"); views.reminders = () => crud("reminders");
views.memory = () => crud("memory"); views.agents = () => crud("agents"); views.automations = () => crud("automations");

views.tools = () => {
  let tab = "tr"; const tabs = {tr: "অনুবাদ", su: "সারসংক্ষেপ", re: "রিসার্চ/সার্চ"};
  const run = async (btn, out, prompt) => { btn.disabled = true; out.textContent = "…"; try { out.innerHTML = md(await ask([{role: "user", content: prompt}], [], {sys: "You are a precise assistant. Follow the instruction exactly."})); } catch (e) { out.textContent = "ত্রুটি: " + e.message; } btn.disabled = false; };
  const draw = () => {
    $("#main").innerHTML = `<h1>টুলস</h1><div class="tabs">${Object.entries(tabs).map(([k, l]) => `<button class="btn sm ${k === tab ? "on" : ""}" data-t="${k}">${l}</button>`).join("")}</div><div class="card">${tab === "tr" ? `<textarea id="in" rows="5" placeholder="অনুবাদের লেখা"></textarea><select id="to"><option>Bengali</option><option>English</option><option>Hindi</option><option>Arabic</option></select><button id="go" class="btn">অনুবাদ করুন</button><div class="out" id="o"></div><button id="sp" class="btn ghost" hidden>${ic("mic")} শুনুন</button>` : tab === "su" ? `<textarea id="in" rows="8" placeholder="ডকুমেন্টের লেখা পেস্ট করুন"></textarea><button id="go" class="btn">সারসংক্ষেপ</button><div class="out" id="o"></div>` : `<input id="in" placeholder="বিষয়"><button id="go" class="btn">AI রিসার্চ ব্রিফ</button><button id="ws" class="btn ghost">ওয়েবে সার্চ (DuckDuckGo)</button><small>AI ব্রিফ মডেলের জ্ঞান থেকে আসে, লাইভ ওয়েব নয়। তথ্য নিজে যাচাই করুন।</small><div class="out" id="o"></div>`}</div>`;
    document.querySelectorAll("[data-t]").forEach(b => b.onclick = () => { tab = b.dataset.t; draw(); });
    $("#go").onclick = e => { const v = $("#in").value.trim(); if (!v) return;
      run(e.target, $("#o"), tab === "tr" ? `Translate the following text into ${$("#to").value}. Output only the translation:\n\n${v}` : tab === "su" ? `Summarize the following text with key points (reply in the text's language):\n\n${v.slice(0, 24000)}` : `Prepare a structured research brief on: ${v}\nInclude key facts, open questions and what to verify. Do not invent sources or URLs.`).then(() => { const s = $("#sp"); if (s) { s.hidden = false; s.onclick = () => speak($("#o").textContent); } }); };
    if (tab === "re") $("#ws").onclick = () => { const v = $("#in").value.trim(); if (v) open("https://duckduckgo.com/?q=" + encodeURIComponent(v), "_blank", "noopener"); };
  };
  draw();
};

views.files = () => {
  $("#main").innerHTML = `<h1>PDF ও ফাইল</h1><div class="card"><input type="file" id="pf" accept="application/pdf"><small>PDF আপনার ডিভাইসেই পড়া হয়। Firebase Storage ব্যবহার করা হয়নি (Blaze প্ল্যান লাগে)। শুধু টেক্সট ও সারসংক্ষেপ Database-এ সেভ হয়।</small></div><div id="rd"></div><h3>সেভ করা ফাইল</h3><div id="fl" class="list"></div>`;
  let doc = null, pg = 0;
  const lib = () => new Promise((res, rej) => { if (window.pdfjsLib) return res(); const s = document.createElement("script"); s.src = "https://cdnjs.cloudflare.com/ajax/libs/pdf.js/3.11.174/pdf.min.js"; s.onload = () => { pdfjsLib.GlobalWorkerOptions.workerSrc = "https://cdnjs.cloudflare.com/ajax/libs/pdf.js/3.11.174/pdf.worker.min.js"; res(); }; s.onerror = () => rej(new Error("pdf.js লোড হয়নি")); document.head.appendChild(s); });
  const show = () => {
    if (!doc) return; const all = doc.pages.join("\n");
    $("#rd").innerHTML = `<div class="card"><b>${esc(doc.name)}</b><small>${doc.pages.length} পৃষ্ঠা</small><div class="out" style="max-height:260px;overflow:auto">${esc(doc.pages[pg])}</div><div class="row"><button id="pp" class="btn sm ghost">‹</button><span>${pg + 1}/${doc.pages.length}</span><button id="pn" class="btn sm ghost">›</button></div>
    <button id="ds" class="btn">সারসংক্ষেপ</button><div class="row"><input id="dq" placeholder="ডকুমেন্ট নিয়ে প্রশ্ন…" style="flex:1"><button id="da" class="btn sm">${ic("send")}</button></div><div class="out" id="do"></div><button id="dv" class="btn ghost">${ic("file")} সেভ করুন</button><small>বড় ডকুমেন্টের শুধু প্রথম ~24,000 অক্ষর AI-কে পাঠানো হয়।</small></div>`;
    $("#pp").onclick = () => { pg = Math.max(0, pg - 1); show(); }; $("#pn").onclick = () => { pg = Math.min(doc.pages.length - 1, pg + 1); show(); };
    const ai = async (b, q) => { b.disabled = true; $("#do").textContent = "…"; try { doc.summary = await ask([{role: "user", content: `${q}\n\nDOCUMENT:\n${all.slice(0, 24000)}`}], [], {sys: "Answer only from the document. If the answer is not in it, say so."}); $("#do").innerHTML = md(doc.summary); } catch (e) { $("#do").textContent = "ত্রুটি: " + e.message; } b.disabled = false; };
    $("#ds").onclick = e => ai(e.target, "Summarize this document with key points."); $("#da").onclick = e => { const q = $("#dq").value.trim(); if (q) ai(e.currentTarget, "Question: " + q); };
    $("#dv").onclick = async () => { try { await D.add("files", {name: doc.name, pages: doc.pages.length, summary: doc.summary || "", text: all.slice(0, 50000)}); toast("সেভ হয়েছে"); } catch (e) { toast(e.message); } };
  };
  $("#pf").onchange = async e => {
    const f = e.target.files[0]; if (!f) return; toast("পড়া হচ্ছে…");
    try { await lib(); const pdf = await pdfjsLib.getDocument({data: await f.arrayBuffer()}).promise, pages = [];
      for (let i = 1; i <= pdf.numPages; i++) pages.push((await (await pdf.getPage(i)).getTextContent()).items.map(x => x.str).join(" "));
      if (pages.join("").trim().length < 20) return toast("টেক্সট পাওয়া যায়নি (স্ক্যান করা PDF; OCR সাপোর্ট নেই)", 6000);
      doc = {name: f.name, pages}; pg = 0; show(); } catch (err) { toast("PDF ত্রুটি: " + err.message, 6000); }
  };
  const draw = () => { const fs = list("files"); $("#fl").innerHTML = fs.length ? fs.map(x => `<div class="item" data-id="${x.id}"><div class="grow"><b>${esc(x.name)}</b><small>${x.pages} পৃষ্ঠা · ${esc((x.summary || "").slice(0, 120))}</small></div><button class="btn sm" data-a="open">খুলুন</button><button class="btn icon ghost" data-a="del">${ic("trash")}</button></div>`).join("") : '<p class="empty">কিছু নেই</p>'; };
  onData = draw; draw();
  $("#fl").onclick = async e => { const b = e.target.closest("[data-a]"); if (!b) return; const id = b.closest(".item").dataset.id, x = C.files[id];
    if (b.dataset.a === "del" && confirm("মুছবেন?")) await D.del("files/" + id);
    if (b.dataset.a === "open") { doc = {name: x.name, pages: (x.text || "").match(/[\s\S]{1,3000}/g) || [""], summary: x.summary}; pg = 0; show(); scrollTo(0, 0); } };
};

views.settings = () => {
  const F = [{k:"callName",l:"আমাকে কী নামে ডাকবে",req:1},{k:"lang",l:"ভয়েস ভাষা",t:"select",o:["bn-BD","en-US"]},{k:"voiceReply",l:"কথা বলে উত্তর দিক",t:"check"},{k:"provider",l:"AI provider",t:"select",o:["ollama","proxy"]},{k:"endpoint",l:"Endpoint (ollama URL বা আপনার Worker URL)"},{k:"model",l:"Model"},{k:"sens",l:"Clap sensitivity (1–10)",t:"range",a:'min="1" max="10"'}];
  $("#main").innerHTML = `<h1>সেটিংস</h1><form id="sf" class="card">${F.map(fieldHtml).join("")}<div class="row"><button class="btn prim">${ic("check")} সেভ</button><button type="button" id="lm" class="btn ghost">Model তালিকা/টেস্ট</button></div></form>
  <div class="card"><h3>ভয়েস ও প্রাইভেসি</h3><div class="row"><button id="ck" class="btn">${ic("clap")} <span id="claplbl"></span></button><button id="nt" class="btn ghost">${ic("bell")} নোটিফিকেশন অনুমতি</button></div>
  <small>Clap শোনার জন্য মাইক খোলা থাকে এবং হেডারে সবসময় "মাইক চালু" দেখা যায়। অডিও রেকর্ড, সেভ বা আপলোড হয় না। শুধু ভলিউম মাপা হয়। ব্রাউজার ট্যাব ব্যাকগ্রাউন্ডে গেলে বা স্ক্রিন বন্ধ হলে Android/Chrome মাইক বন্ধ করে দেয়। তাই এটি "always-on" নয়। Speech recognition Chrome-এর সার্ভিস ব্যবহার করে (অডিও Google-এ যেতে পারে)। এটি ${supported.sr ? "এই ব্রাউজারে আছে" : "এই ব্রাউজারে নেই"}।</small></div>
  <div class="card"><h3>আপনার ডেটা</h3><div class="row"><button id="ex" class="btn ghost">JSON এক্সপোর্ট</button><button id="wp" class="btn ghost" style="color:#b91c1c">সব ডেটা মুছুন</button></div></div>`;
  const f = $("#sf"); F.forEach(q => setField(f, q, S[q.k])); setBadge();
  f.onsubmit = async e => { e.preventDefault(); const v = {}; F.forEach(q => v[q.k] = getField(f, q)); try { await D.patch("settings", v); Object.assign(S, v); toast("সেভ হয়েছে"); } catch (err) { toast("সেভ হয়নি: " + err.message, 6000); } };
  $("#lm").onclick = async () => { const v = {}; F.forEach(q => v[q.k] = getField(f, q)); Object.assign(S, v); try { if (S.provider === "ollama") { const m = await listModels(); toast(m.length ? "Models: " + m.join(", ") : "কোনো model নেই — ollama pull করুন", 7000); } else { const r = await ask([{role: "user", content: "Reply with: ok"}], [], {sys: "Reply briefly."}); toast("Proxy উত্তর: " + r.slice(0, 40)); } } catch (e) { toast("সংযোগ ব্যর্থ: " + e.message, 7000); } };
  $("#ck").onclick = toggleClap;
  $("#nt").onclick = async () => toast("অনুমতি: " + await Notification.requestPermission());
  $("#ex").onclick = async () => { const a = document.createElement("a"); a.href = URL.createObjectURL(new Blob([JSON.stringify(await D.all(), null, 2)], {type: "application/json"})); a.download = "mayra-data.json"; a.click(); };
  $("#wp").onclick = async () => { if (confirm("আপনার সব ডেটা স্থায়ীভাবে মুছে যাবে। নিশ্চিত?")) { await D.wipe(); toast("মুছে ফেলা হয়েছে। (Auth অ্যাকাউন্ট Firebase Console থেকে মুছুন)", 7000); booted = false; A.logout(); } };
};
'''

# ───────────────────────── Firebase / deploy config ─────────────────────────
FILES["firebase.json"] = r'''{
  "database": {"rules": "database.rules.json"},
  "hosting": {
    "public": "public",
    "ignore": ["firebase.json", "**/.*", "**/node_modules/**"],
    "headers": [
      {"source": "**/*.@(js|css)", "headers": [{"key": "Cache-Control", "value": "no-cache"}]},
      {"source": "**", "headers": [
        {"key": "X-Content-Type-Options", "value": "nosniff"},
        {"key": "Referrer-Policy", "value": "strict-origin-when-cross-origin"},
        {"key": "Permissions-Policy", "value": "microphone=(self), camera=()"}
      ]}
    ]
  }
}
'''
FILES["database.rules.json"] = r'''{
  "rules": {
    ".read": false,
    ".write": false,
    "users": {
      "$uid": {
        ".read": "auth != null && auth.uid === $uid",
        ".write": "auth != null && auth.uid === $uid",
        "profile": {".validate": "newData.hasChildren(['createdAt'])"},
        "settings": {
          "callName": {".validate": "newData.isString() && newData.val().length <= 40"},
          "sens": {".validate": "newData.isNumber() && newData.val() >= 1 && newData.val() <= 10"}
        }
      }
    }
  }
}
'''
FILES[".firebaserc"] = r'''{"projects": {"default": "YOUR_FIREBASE_PROJECT_ID"}}
'''
FILES[".gitignore"] = r'''node_modules/
.firebase/
*.log
sa.json
.dev.vars
'''
FILES[".github/workflows/deploy.yml"] = r'''name: Deploy MAYRA
on:
  push:
    branches: [main]
  workflow_dispatch:
jobs:
  deploy:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-node@v4
        with: {node-version: 20}
      - run: npm i -g firebase-tools
      - name: Write service account
        env:
          SA: ${{ secrets.FIREBASE_SERVICE_ACCOUNT }}
        run: echo "$SA" > "$RUNNER_TEMP/sa.json"
      - name: Deploy hosting + database rules
        env:
          GOOGLE_APPLICATION_CREDENTIALS: ${{ runner.temp }}/sa.json
        run: firebase deploy --only hosting,database --project "${{ secrets.FIREBASE_PROJECT_ID }}" --non-interactive
'''

# ───────────────────────── AI proxy (free Cloudflare Worker) ─────────────────────────
FILES["worker/worker.js"] = r'''// Free AI proxy: keeps the secret AI key OUT of the frontend.
// Only signed-in Firebase users can call it (ID token is verified with Google).
// Secrets/vars (Cloudflare dashboard → Worker → Settings): UPSTREAM_URL, UPSTREAM_KEY, FIREBASE_WEB_API_KEY, ALLOWED_ORIGIN, DEFAULT_MODEL
export default {
  async fetch(req, env) {
    const cors = {"Access-Control-Allow-Origin": env.ALLOWED_ORIGIN || "*", "Access-Control-Allow-Headers": "Authorization,Content-Type", "Access-Control-Allow-Methods": "POST,OPTIONS"};
    if (req.method === "OPTIONS") return new Response(null, {headers: cors});
    if (req.method !== "POST") return new Response("Method not allowed", {status: 405, headers: cors});
    const tok = (req.headers.get("Authorization") || "").replace(/^Bearer /, "");
    if (!tok) return new Response("Unauthorized", {status: 401, headers: cors});
    const v = await fetch(`https://identitytoolkit.googleapis.com/v1/accounts:lookup?key=${env.FIREBASE_WEB_API_KEY}`, {method: "POST", headers: {"Content-Type": "application/json"}, body: JSON.stringify({idToken: tok})});
    if (!v.ok) return new Response("Invalid token", {status: 401, headers: cors});
    const b = await req.json(); b.stream = false; if (!b.model) b.model = env.DEFAULT_MODEL;
    const r = await fetch(env.UPSTREAM_URL, {method: "POST", headers: {"Content-Type": "application/json", Authorization: "Bearer " + env.UPSTREAM_KEY}, body: JSON.stringify(b)});
    return new Response(r.body, {status: r.status, headers: {...cors, "Content-Type": "application/json"}});
  }
};
'''
FILES["worker/wrangler.toml"] = r'''name = "mayra-ai-proxy"
main = "worker.js"
compatibility_date = "2024-11-01"
'''

# ───────────────────────── README ─────────────────────────
FILES["README.md"] = r'''# MAYRA — Your Personal AI Assistant

Bengali + English personal assistant: AI chat, voice, Clap-to-Wake, memory, planner, tasks, notes, calendar, reminders, automations, AI agents, PDF assistant, translation, summarization, research.
Stack: static HTML/CSS/JS (no build step) + Firebase Hosting / Auth / Realtime Database. Free (Spark) plan.

## ১. Firebase (ফোন থেকেই, console.firebase.google.com)
1. নতুন প্রজেক্ট খুলুন → Build → **Authentication** → Email/Password ও Google চালু করুন।
2. **Realtime Database** তৈরি করুন (locked mode)। Rules পরে GitHub deploy-এ আসবে।
3. **Hosting** চালু করুন।
4. Project settings → Web app (`</>`) যোগ করুন → `firebaseConfig` কপি করে `public/js/firebase-config.js`-এ বসান।
5. `.firebaserc`-এ `YOUR_FIREBASE_PROJECT_ID` বদলান।
6. Authentication → Settings → Authorized domains-এ আপনার `*.web.app` আছে কিনা দেখুন।

## ২. GitHub থেকে অটো ডিপ্লয়
1. Firebase Console → Project settings → Service accounts → **Generate new private key** (JSON)।
2. GitHub repo → Settings → Secrets → Actions: `FIREBASE_SERVICE_ACCOUNT` = পুরো JSON, `FIREBASE_PROJECT_ID` = প্রজেক্ট আইডি।
3. IAM-এ ওই service account-কে *Firebase Admin* (বা Hosting Admin + Realtime Database Admin) রোল দিন।
4. `main` ব্রাঞ্চে push করলেই Hosting ও Database Rules deploy হবে।

## ৩. AI (ফ্রি, কী ফ্রন্টএন্ডে নেই)
- **Ollama (লোকাল):** PC/ফোনে Ollama চালান, `OLLAMA_ORIGINS=https://YOUR-APP.web.app` সেট করে `ollama pull llama3.2`। Settings → provider `ollama`, endpoint `http://localhost:11434`। (শুধু যে ডিভাইসে Ollama চলছে সেখানেই কাজ করে।)
- **Proxy (যেকোনো ডিভাইস):** `worker/` ফোল্ডারটি Cloudflare Workers-এ (ফ্রি) deploy করুন। Variables: `UPSTREAM_URL` (যেমন Groq/OpenAI-compatible `.../chat/completions`), `UPSTREAM_KEY` (আপনার ফ্রি-টিয়ার কী, secret), `FIREBASE_WEB_API_KEY`, `ALLOWED_ORIGIN`, `DEFAULT_MODEL`। Settings → provider `proxy`, endpoint = Worker URL। Worker Firebase ID token যাচাই করে।
- AI কনফিগার না থাকলে Mayra স্পষ্ট এরর দেখায়, নকল উত্তর দেয় না।

## ডেটা কাঠামো
`users/{uid}/profile | settings | chats | chatMessages | memory | tasks | notes | reminders | automations(+history) | agents | files` — সবকিছু শুধু মালিকের জন্য (`database.rules.json`)। `chatMessages` আলাদা রাখা হয়েছে যাতে চ্যাট তালিকা লোড করতে সব মেসেজ নামাতে না হয়।

## সীমাবদ্ধতা (সৎ তথ্য)
- **Clap/ভয়েস:** ব্রাউজার ব্যাকগ্রাউন্ডে মাইক দেয় না। ট্যাব খোলা + স্ক্রিন অন লাগবে। মাইক চালু থাকলে হেডারে সবসময় দেখায়; অডিও সেভ হয় না। ক্ল্যাপের পর স্বয়ংক্রিয় শোনা কিছু ব্রাউজারে ট্যাপ চাইতে পারে (🎙 বাটন আছে)। Speech recognition Chrome/Edge-এ ভালো।
- **অটোমেশন ও রিমাইন্ডার:** ব্রাউজারে চলে, অ্যাপ খোলা থাকলেই। বন্ধ থাকলে মিস হওয়া রিমাইন্ডার পরে খুললে বাজে; daily সময় মিস হলে সেদিনের জন্য চলে না। সার্ভার-সাইড স্কেজুলিং (Cloud Functions) Blaze প্ল্যান লাগে বলে বাদ। প্রতিটি ধাপ লিখে যাচাই করে History-তে সফল/ব্যর্থ রেকর্ড হয়।
- **ফাইল:** Firebase Storage এখন Blaze প্ল্যান চায়, তাই PDF ডিভাইসে পড়া হয়, শুধু টেক্সট/সারসংক্ষেপ Database-এ সেভ হয়। স্ক্যান করা PDF-এ OCR নেই।
- **Research:** মডেলের জ্ঞান থেকে ব্রিফ; লাইভ ওয়েব সার্চ নয় (DuckDuckGo লিংক দেওয়া আছে)।

## ফোনে এডিট
GitHub অ্যাপ/ব্রাউজারে ফাইল খুলে সরাসরি এডিট → commit → অটো deploy। মূল লজিক: `public/js/app.js` (UI), `core.js` (Firebase), `ai.js`, `voice.js`।
'''


def main():
    args = [a for a in sys.argv[1:]]
    if "--list" in args:
        for p in FILES: print(p)
        return
    root = pathlib.Path(args[0] if args else "mayra")
    for rel, content in FILES.items():
        f = root / rel
        f.parent.mkdir(parents=True, exist_ok=True)
        f.write_text(content.lstrip("\n"), encoding="utf-8")
        print("created", f)
    print(f"\nDone: {len(FILES)} files in ./{root}\nNext: open {root}/README.md")


if __name__ == "__main__":
    main()
