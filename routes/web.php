<?php

use Illuminate\Support\Facades\Route;

/*
|--------------------------------------------------------------------------
| Web Routes
|--------------------------------------------------------------------------
|
| Here is where you can register web routes for your application. These
| routes are loaded by the RouteServiceProvider and all of them will
| be assigned to the "web" middleware group. Make something great!
|
*/

Route::domain(parse_url(env('APP_URL', 'http://da.adlynk.in.test'), PHP_URL_HOST))->group(function () {
    Route::get('/', [App\Http\Controllers\Caller\LoginController::class, 'index']);
    Route::get('login', [App\Http\Controllers\Caller\LoginController::class, 'index'])->name('login');
    Route::post('login', [App\Http\Controllers\Caller\LoginController::class, 'validateUser']);
    Route::get('login/{driver}/start', [App\Http\Controllers\Caller\LoginController::class, 'redirectToProvider']);
    Route::any('login/{driver}/callback', [App\Http\Controllers\Caller\LoginController::class, 'handleProviderCallback']);
    Route::any('logout', [App\Http\Controllers\Caller\LoginController::class, 'Logout']);
    Route::get('html-page', function () {
        return view('app-calendar');
    });
    Route::middleware(['auth:web'])->group(function () {
    });
});

