import sys
import re

file_path = r'c:\Users\ARDI\.gemini\antigravity-ide\scratch\ardi-portfolio\schedule.html'

with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

new_html = '''                <!-- GRID OF DAYS -->
                <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">

                    <!-- SENIN -->
                    <div class="day-card rounded-2xl bg-om-card-light dark:bg-om-card-dark border border-om-gold/30 p-6 shadow-xl" data-day-name="SENIN">
                        <div class="flex items-center justify-between border-b border-om-gold/20 pb-3 mb-4">
                            <h3 class="font-serif text-xl font-bold text-om-navy dark:text-om-gold flex items-center gap-2">
                                <i class="fa-solid fa-flag text-sm"></i> SENIN
                            </h3>
                            <span class="text-[10px] uppercase font-bold px-2 py-0.5 rounded bg-om-gold/20 text-om-gold">Jadwal Sekolah</span>
                        </div>
                        <ul class="space-y-2 text-xs">
                            <li class="p-2 rounded bg-om-cream/70 dark:bg-om-navy/40 flex flex-col sm:flex-row justify-between items-start sm:items-center">
                                <span class="font-semibold text-gray-500 dark:text-gray-400 mb-1 sm:mb-0">06.30 - 07.30</span>
                                <span class="font-bold text-om-navy dark:text-white sm:text-right block">UPACARA / WALI KELAS</span>
                            </li>
                            <li class="p-2 rounded bg-om-cream/70 dark:bg-om-navy/40 flex flex-col sm:flex-row justify-between items-start sm:items-center">
                                <span class="font-semibold text-gray-500 dark:text-gray-400 mb-1 sm:mb-0">07.30 - 08.15</span>
                                <div class="text-left sm:text-right">
                                    <span class="font-bold text-om-navy dark:text-white block">SOSIOLOGI</span>
                                    <span class="text-[10px] font-normal text-gray-500 dark:text-gray-400 block">Cornel Kaban</span>
                                </div>
                            </li>
                            <li class="p-2 rounded bg-om-cream/70 dark:bg-om-navy/40 flex flex-col sm:flex-row justify-between items-start sm:items-center">
                                <span class="font-semibold text-gray-500 dark:text-gray-400 mb-1 sm:mb-0">08.15 - 09.00</span>
                                <div class="text-left sm:text-right">
                                    <span class="font-bold text-om-navy dark:text-white block">SOSIOLOGI</span>
                                    <span class="text-[10px] font-normal text-gray-500 dark:text-gray-400 block">Cornel Kaban</span>
                                </div>
                            </li>
                            <li class="p-2 rounded bg-amber-500/10 text-amber-700 dark:text-amber-300 flex justify-between items-center font-bold">
                                <span>09.00 - 09.30</span>
                                <span>ISTIRAHAT</span>
                            </li>
                            <li class="p-2 rounded bg-om-cream/70 dark:bg-om-navy/40 flex flex-col sm:flex-row justify-between items-start sm:items-center">
                                <span class="font-semibold text-gray-500 dark:text-gray-400 mb-1 sm:mb-0">09.30 - 10.10</span>
                                <div class="text-left sm:text-right">
                                    <span class="font-bold text-om-navy dark:text-white block">MANDARIN</span>
                                    <span class="text-[10px] font-normal text-gray-500 dark:text-gray-400 block">Junaidi</span>
                                </div>
                            </li>
                            <li class="p-2 rounded bg-om-cream/70 dark:bg-om-navy/40 flex flex-col sm:flex-row justify-between items-start sm:items-center">
                                <span class="font-semibold text-gray-500 dark:text-gray-400 mb-1 sm:mb-0">10.10 - 10.50</span>
                                <div class="text-left sm:text-right">
                                    <span class="font-bold text-om-navy dark:text-white block">MANDARIN</span>
                                    <span class="text-[10px] font-normal text-gray-500 dark:text-gray-400 block">Junaidi</span>
                                </div>
                            </li>
                            <li class="p-2 rounded bg-om-cream/70 dark:bg-om-navy/40 flex flex-col sm:flex-row justify-between items-start sm:items-center">
                                <span class="font-semibold text-gray-500 dark:text-gray-400 mb-1 sm:mb-0">10.50 - 11.30</span>
                                <div class="text-left sm:text-right">
                                    <span class="font-bold text-om-navy dark:text-white block">BUDI PEKERTI</span>
                                    <span class="text-[10px] font-normal text-gray-500 dark:text-gray-400 block">Suwarni</span>
                                </div>
                            </li>
                            <li class="p-2 rounded bg-om-cream/70 dark:bg-om-navy/40 flex flex-col sm:flex-row justify-between items-start sm:items-center">
                                <span class="font-semibold text-gray-500 dark:text-gray-400 mb-1 sm:mb-0">11.30 - 12.10</span>
                                <div class="text-left sm:text-right">
                                    <span class="font-bold text-om-navy dark:text-white block">B. HUMANIS</span>
                                    <span class="text-[10px] font-normal text-gray-500 dark:text-gray-400 block">Iriwaty Japutra</span>
                                </div>
                            </li>
                            <li class="p-2 rounded bg-amber-500/10 text-amber-700 dark:text-amber-300 flex justify-between items-center font-bold">
                                <span>12.10 - 12.40</span>
                                <span>ISTIRAHAT</span>
                            </li>
                            <li class="p-2 rounded bg-om-cream/70 dark:bg-om-navy/40 flex flex-col sm:flex-row justify-between items-start sm:items-center">
                                <span class="font-semibold text-gray-500 dark:text-gray-400 mb-1 sm:mb-0">12.40 - 13.20</span>
                                <div class="text-left sm:text-right">
                                    <span class="font-bold text-om-navy dark:text-white block">MATEMATIKA WAJIB</span>
                                    <span class="text-[10px] font-normal text-gray-500 dark:text-gray-400 block">Jefry Corpry YH</span>
                                </div>
                            </li>
                            <li class="p-2 rounded bg-om-cream/70 dark:bg-om-navy/40 flex flex-col sm:flex-row justify-between items-start sm:items-center">
                                <span class="font-semibold text-gray-500 dark:text-gray-400 mb-1 sm:mb-0">13.20 - 14.00</span>
                                <div class="text-left sm:text-right">
                                    <span class="font-bold text-om-navy dark:text-white block">EKONOMI</span>
                                    <span class="text-[10px] font-normal text-gray-500 dark:text-gray-400 block">Debie Lola</span>
                                </div>
                            </li>
                            <li class="p-2 rounded bg-om-cream/70 dark:bg-om-navy/40 flex flex-col sm:flex-row justify-between items-start sm:items-center">
                                <span class="font-semibold text-gray-500 dark:text-gray-400 mb-1 sm:mb-0">14.00 - 14.40</span>
                                <div class="text-left sm:text-right">
                                    <span class="font-bold text-om-navy dark:text-white block">EKONOMI</span>
                                    <span class="text-[10px] font-normal text-gray-500 dark:text-gray-400 block">Debie Lola</span>
                                </div>
                            </li>
                        </ul>
                    </div>

                    <!-- SELASA -->
                    <div class="day-card rounded-2xl bg-om-card-light dark:bg-om-card-dark border border-om-gold/30 p-6 shadow-xl" data-day-name="SELASA">
                        <div class="flex items-center justify-between border-b border-om-gold/20 pb-3 mb-4">
                            <h3 class="font-serif text-xl font-bold text-om-navy dark:text-om-gold flex items-center gap-2">
                                <i class="fa-solid fa-book text-sm"></i> SELASA
                            </h3>
                            <span class="text-[10px] uppercase font-bold px-2 py-0.5 rounded bg-om-gold/20 text-om-gold">Jadwal Sekolah</span>
                        </div>
                        <ul class="space-y-2 text-xs">
                            <li class="p-2 rounded bg-om-cream/70 dark:bg-om-navy/40 flex flex-col sm:flex-row justify-between items-start sm:items-center">
                                <span class="font-semibold text-gray-500 dark:text-gray-400 mb-1 sm:mb-0">06.30 - 06.45</span>
                                <span class="font-bold text-om-navy dark:text-white sm:text-right block">PEMBIASAAN AWAL</span>
                            </li>
                            <li class="p-2 rounded bg-om-cream/70 dark:bg-om-navy/40 flex flex-col sm:flex-row justify-between items-start sm:items-center">
                                <span class="font-semibold text-gray-500 dark:text-gray-400 mb-1 sm:mb-0">06.45 - 07.30</span>
                                <div class="text-left sm:text-right">
                                    <span class="font-bold text-om-navy dark:text-white block">AGAMA</span>
                                    <span class="text-[10px] font-normal text-gray-500 dark:text-gray-400 block">Suwarni</span>
                                </div>
                            </li>
                            <li class="p-2 rounded bg-om-cream/70 dark:bg-om-navy/40 flex flex-col sm:flex-row justify-between items-start sm:items-center">
                                <span class="font-semibold text-gray-500 dark:text-gray-400 mb-1 sm:mb-0">07.30 - 08.15</span>
                                <div class="text-left sm:text-right">
                                    <span class="font-bold text-om-navy dark:text-white block">AGAMA</span>
                                    <span class="text-[10px] font-normal text-gray-500 dark:text-gray-400 block">Suwarni</span>
                                </div>
                            </li>
                            <li class="p-2 rounded bg-om-cream/70 dark:bg-om-navy/40 flex flex-col sm:flex-row justify-between items-start sm:items-center">
                                <span class="font-semibold text-gray-500 dark:text-gray-400 mb-1 sm:mb-0">08.15 - 09.00</span>
                                <div class="text-left sm:text-right">
                                    <span class="font-bold text-om-navy dark:text-white block">B. INDONESIA</span>
                                    <span class="text-[10px] font-normal text-gray-500 dark:text-gray-400 block">Ruly Mediana</span>
                                </div>
                            </li>
                            <li class="p-2 rounded bg-om-cream/70 dark:bg-om-navy/40 flex flex-col sm:flex-row justify-between items-start sm:items-center">
                                <span class="font-semibold text-gray-500 dark:text-gray-400 mb-1 sm:mb-0">09.00 - 09.45</span>
                                <div class="text-left sm:text-right">
                                    <span class="font-bold text-om-navy dark:text-white block">B. INDONESIA</span>
                                    <span class="text-[10px] font-normal text-gray-500 dark:text-gray-400 block">Ruly Mediana</span>
                                </div>
                            </li>
                            <li class="p-2 rounded bg-amber-500/10 text-amber-700 dark:text-amber-300 flex justify-between items-center font-bold">
                                <span>09.45 - 10.05</span>
                                <span>ISTIRAHAT</span>
                            </li>
                            <li class="p-2 rounded bg-om-cream/70 dark:bg-om-navy/40 flex flex-col sm:flex-row justify-between items-start sm:items-center">
                                <span class="font-semibold text-gray-500 dark:text-gray-400 mb-1 sm:mb-0">10.05 - 10.50</span>
                                <div class="text-left sm:text-right">
                                    <span class="font-bold text-om-navy dark:text-white block">GEOGRAFI</span>
                                    <span class="text-[10px] font-normal text-gray-500 dark:text-gray-400 block">Nur Fajar Sidik</span>
                                </div>
                            </li>
                            <li class="p-2 rounded bg-om-cream/70 dark:bg-om-navy/40 flex flex-col sm:flex-row justify-between items-start sm:items-center">
                                <span class="font-semibold text-gray-500 dark:text-gray-400 mb-1 sm:mb-0">10.50 - 11.35</span>
                                <div class="text-left sm:text-right">
                                    <span class="font-bold text-om-navy dark:text-white block">GEOGRAFI</span>
                                    <span class="text-[10px] font-normal text-gray-500 dark:text-gray-400 block">Nur Fajar Sidik</span>
                                </div>
                            </li>
                            <li class="p-2 rounded bg-amber-500/10 text-amber-700 dark:text-amber-300 flex justify-between items-center font-bold">
                                <span>11.35 - 12.00</span>
                                <span>ISTIRAHAT</span>
                            </li>
                            <li class="p-2 rounded bg-om-cream/70 dark:bg-om-navy/40 flex flex-col sm:flex-row justify-between items-start sm:items-center">
                                <span class="font-semibold text-gray-500 dark:text-gray-400 mb-1 sm:mb-0">12.00 - 12.40</span>
                                <div class="text-left sm:text-right">
                                    <span class="font-bold text-om-navy dark:text-white block">EKONOMI</span>
                                    <span class="text-[10px] font-normal text-gray-500 dark:text-gray-400 block">Debie Lola</span>
                                </div>
                            </li>
                            <li class="p-2 rounded bg-om-cream/70 dark:bg-om-navy/40 flex flex-col sm:flex-row justify-between items-start sm:items-center">
                                <span class="font-semibold text-gray-500 dark:text-gray-400 mb-1 sm:mb-0">12.40 - 13.20</span>
                                <div class="text-left sm:text-right">
                                    <span class="font-bold text-om-navy dark:text-white block">EKONOMI</span>
                                    <span class="text-[10px] font-normal text-gray-500 dark:text-gray-400 block">Debie Lola</span>
                                </div>
                            </li>
                            <li class="p-2 rounded bg-om-cream/70 dark:bg-om-navy/40 flex flex-col sm:flex-row justify-between items-start sm:items-center">
                                <span class="font-semibold text-gray-500 dark:text-gray-400 mb-1 sm:mb-0">13.20 - 14.00</span>
                                <div class="text-left sm:text-right">
                                    <span class="font-bold text-om-navy dark:text-white block">SOSIOLOGI</span>
                                    <span class="text-[10px] font-normal text-gray-500 dark:text-gray-400 block">Cornel Kaban</span>
                                </div>
                            </li>
                            <li class="p-2 rounded bg-om-cream/70 dark:bg-om-navy/40 flex flex-col sm:flex-row justify-between items-start sm:items-center">
                                <span class="font-semibold text-gray-500 dark:text-gray-400 mb-1 sm:mb-0">14.00 - 14.30</span>
                                <div class="text-left sm:text-right">
                                    <span class="font-bold text-om-navy dark:text-white block">SOSIOLOGI</span>
                                    <span class="text-[10px] font-normal text-gray-500 dark:text-gray-400 block">Cornel Kaban</span>
                                </div>
                            </li>
                        </ul>
                    </div>

                    <!-- RABU -->
                    <div class="day-card rounded-2xl bg-om-card-light dark:bg-om-card-dark border border-om-gold/30 p-6 shadow-xl" data-day-name="RABU">
                        <div class="flex items-center justify-between border-b border-om-gold/20 pb-3 mb-4">
                            <h3 class="font-serif text-xl font-bold text-om-navy dark:text-om-gold flex items-center gap-2">
                                <i class="fa-solid fa-palette text-sm"></i> RABU
                            </h3>
                            <span class="text-[10px] uppercase font-bold px-2 py-0.5 rounded bg-om-gold/20 text-om-gold">Jadwal Sekolah</span>
                        </div>
                        <ul class="space-y-2 text-xs">
                            <li class="p-2 rounded bg-om-cream/70 dark:bg-om-navy/40 flex flex-col sm:flex-row justify-between items-start sm:items-center">
                                <span class="font-semibold text-gray-500 dark:text-gray-400 mb-1 sm:mb-0">06.30 - 06.45</span>
                                <span class="font-bold text-om-navy dark:text-white sm:text-right block">PEMBIASAAN AWAL</span>
                            </li>
                            <li class="p-2 rounded bg-om-cream/70 dark:bg-om-navy/40 flex flex-col sm:flex-row justify-between items-start sm:items-center">
                                <span class="font-semibold text-gray-500 dark:text-gray-400 mb-1 sm:mb-0">06.45 - 07.30</span>
                                <div class="text-left sm:text-right">
                                    <span class="font-bold text-om-navy dark:text-white block">INFORMATIKA</span>
                                    <span class="text-[10px] font-normal text-gray-500 dark:text-gray-400 block">Yahya Yanuardi</span>
                                </div>
                            </li>
                            <li class="p-2 rounded bg-om-cream/70 dark:bg-om-navy/40 flex flex-col sm:flex-row justify-between items-start sm:items-center">
                                <span class="font-semibold text-gray-500 dark:text-gray-400 mb-1 sm:mb-0">07.30 - 08.15</span>
                                <div class="text-left sm:text-right">
                                    <span class="font-bold text-om-navy dark:text-white block">INFORMATIKA</span>
                                    <span class="text-[10px] font-normal text-gray-500 dark:text-gray-400 block">Yahya Yanuardi</span>
                                </div>
                            </li>
                            <li class="p-2 rounded bg-om-cream/70 dark:bg-om-navy/40 flex flex-col sm:flex-row justify-between items-start sm:items-center">
                                <span class="font-semibold text-gray-500 dark:text-gray-400 mb-1 sm:mb-0">08.15 - 09.00</span>
                                <div class="text-left sm:text-right">
                                    <span class="font-bold text-om-navy dark:text-white block">MANDARIN</span>
                                    <span class="text-[10px] font-normal text-gray-500 dark:text-gray-400 block">Junaidi</span>
                                </div>
                            </li>
                            <li class="p-2 rounded bg-amber-500/10 text-amber-700 dark:text-amber-300 flex justify-between items-center font-bold">
                                <span>09.00 - 09.30</span>
                                <span>ISTIRAHAT</span>
                            </li>
                            <li class="p-2 rounded bg-om-cream/70 dark:bg-om-navy/40 flex flex-col sm:flex-row justify-between items-start sm:items-center">
                                <span class="font-semibold text-gray-500 dark:text-gray-400 mb-1 sm:mb-0">09.30 - 10.10</span>
                                <div class="text-left sm:text-right">
                                    <span class="font-bold text-om-navy dark:text-white block">MANDARIN</span>
                                    <span class="text-[10px] font-normal text-gray-500 dark:text-gray-400 block">Junaidi</span>
                                </div>
                            </li>
                            <li class="p-2 rounded bg-om-cream/70 dark:bg-om-navy/40 flex flex-col sm:flex-row justify-between items-start sm:items-center">
                                <span class="font-semibold text-gray-500 dark:text-gray-400 mb-1 sm:mb-0">10.10 - 10.50</span>
                                <div class="text-left sm:text-right">
                                    <span class="font-bold text-om-navy dark:text-white block">SOSIOLOGI</span>
                                    <span class="text-[10px] font-normal text-gray-500 dark:text-gray-400 block">Cornel Kaban</span>
                                </div>
                            </li>
                            <li class="p-2 rounded bg-om-cream/70 dark:bg-om-navy/40 flex flex-col sm:flex-row justify-between items-start sm:items-center">
                                <span class="font-semibold text-gray-500 dark:text-gray-400 mb-1 sm:mb-0">10.50 - 11.30</span>
                                <div class="text-left sm:text-right">
                                    <span class="font-bold text-om-navy dark:text-white block">B. INDONESIA</span>
                                    <span class="text-[10px] font-normal text-gray-500 dark:text-gray-400 block">Ruly Mediana</span>
                                </div>
                            </li>
                            <li class="p-2 rounded bg-om-cream/70 dark:bg-om-navy/40 flex flex-col sm:flex-row justify-between items-start sm:items-center">
                                <span class="font-semibold text-gray-500 dark:text-gray-400 mb-1 sm:mb-0">11.30 - 12.10</span>
                                <span class="font-bold text-om-navy dark:text-white sm:text-right block">KOKURIKULER</span>
                            </li>
                            <li class="p-2 rounded bg-amber-500/10 text-amber-700 dark:text-amber-300 flex justify-between items-center font-bold">
                                <span>12.10 - 12.40</span>
                                <span>ISTIRAHAT</span>
                            </li>
                            <li class="p-2 rounded bg-om-cream/70 dark:bg-om-navy/40 flex flex-col sm:flex-row justify-between items-start sm:items-center">
                                <span class="font-semibold text-gray-500 dark:text-gray-400 mb-1 sm:mb-0">12.40 - 13.20</span>
                                <div class="text-left sm:text-right">
                                    <span class="font-bold text-om-navy dark:text-white block">SEJARAH</span>
                                    <span class="text-[10px] font-normal text-gray-500 dark:text-gray-400 block">Cornel Kaban</span>
                                </div>
                            </li>
                            <li class="p-2 rounded bg-om-cream/70 dark:bg-om-navy/40 flex flex-col sm:flex-row justify-between items-start sm:items-center">
                                <span class="font-semibold text-gray-500 dark:text-gray-400 mb-1 sm:mb-0">13.20 - 14.00</span>
                                <div class="text-left sm:text-right">
                                    <span class="font-bold text-om-navy dark:text-white block">SEJARAH</span>
                                    <span class="text-[10px] font-normal text-gray-500 dark:text-gray-400 block">Cornel Kaban</span>
                                </div>
                            </li>
                            <li class="p-2 rounded bg-om-cream/70 dark:bg-om-navy/40 flex flex-col sm:flex-row justify-between items-start sm:items-center">
                                <span class="font-semibold text-gray-500 dark:text-gray-400 mb-1 sm:mb-0">14.00 - 14.40</span>
                                <div class="text-left sm:text-right">
                                    <span class="font-bold text-om-navy dark:text-white block">B. INDONESIA</span>
                                    <span class="text-[10px] font-normal text-gray-500 dark:text-gray-400 block">Ruly Mediana</span>
                                </div>
                            </li>
                            <li class="p-2 rounded bg-om-cream/70 dark:bg-om-navy/40 flex flex-col sm:flex-row justify-between items-start sm:items-center">
                                <span class="font-semibold text-gray-500 dark:text-gray-400 mb-1 sm:mb-0">14.40 - 15.20</span>
                                <div class="text-left sm:text-right">
                                    <span class="font-bold text-om-navy dark:text-white block">B. INDONESIA</span>
                                    <span class="text-[10px] font-normal text-gray-500 dark:text-gray-400 block">Ruly Mediana</span>
                                </div>
                            </li>
                        </ul>
                    </div>

                    <!-- KAMIS -->
                    <div class="day-card rounded-2xl bg-om-card-light dark:bg-om-card-dark border border-om-gold/30 p-6 shadow-xl" data-day-name="KAMIS">
                        <div class="flex items-center justify-between border-b border-om-gold/20 pb-3 mb-4">
                            <h3 class="font-serif text-xl font-bold text-om-navy dark:text-om-gold flex items-center gap-2">
                                <i class="fa-solid fa-earth-americas text-sm"></i> KAMIS
                            </h3>
                            <span class="text-[10px] uppercase font-bold px-2 py-0.5 rounded bg-om-gold/20 text-om-gold">Jadwal Sekolah</span>
                        </div>
                        <ul class="space-y-2 text-xs">
                            <li class="p-2 rounded bg-om-cream/70 dark:bg-om-navy/40 flex flex-col sm:flex-row justify-between items-start sm:items-center">
                                <span class="font-semibold text-gray-500 dark:text-gray-400 mb-1 sm:mb-0">06.30 - 06.45</span>
                                <span class="font-bold text-om-navy dark:text-white sm:text-right block">PEMBIASAAN AWAL</span>
                            </li>
                            <li class="p-2 rounded bg-om-cream/70 dark:bg-om-navy/40 flex flex-col sm:flex-row justify-between items-start sm:items-center">
                                <span class="font-semibold text-gray-500 dark:text-gray-400 mb-1 sm:mb-0">06.45 - 07.30</span>
                                <div class="text-left sm:text-right">
                                    <span class="font-bold text-om-navy dark:text-white block">INFORMATIKA</span>
                                    <span class="text-[10px] font-normal text-gray-500 dark:text-gray-400 block">Yahya Yanuardi</span>
                                </div>
                            </li>
                            <li class="p-2 rounded bg-om-cream/70 dark:bg-om-navy/40 flex flex-col sm:flex-row justify-between items-start sm:items-center">
                                <span class="font-semibold text-gray-500 dark:text-gray-400 mb-1 sm:mb-0">07.30 - 08.15</span>
                                <div class="text-left sm:text-right">
                                    <span class="font-bold text-om-navy dark:text-white block">INFORMATIKA</span>
                                    <span class="text-[10px] font-normal text-gray-500 dark:text-gray-400 block">Yahya Yanuardi</span>
                                </div>
                            </li>
                            <li class="p-2 rounded bg-om-cream/70 dark:bg-om-navy/40 flex flex-col sm:flex-row justify-between items-start sm:items-center">
                                <span class="font-semibold text-gray-500 dark:text-gray-400 mb-1 sm:mb-0">08.15 - 09.00</span>
                                <div class="text-left sm:text-right">
                                    <span class="font-bold text-om-navy dark:text-white block">MATEMATIKA WAJIB</span>
                                    <span class="text-[10px] font-normal text-gray-500 dark:text-gray-400 block">Jefry Corpry YH</span>
                                </div>
                            </li>
                            <li class="p-2 rounded bg-amber-500/10 text-amber-700 dark:text-amber-300 flex justify-between items-center font-bold">
                                <span>09.00 - 09.30</span>
                                <span>ISTIRAHAT</span>
                            </li>
                            <li class="p-2 rounded bg-om-cream/70 dark:bg-om-navy/40 flex flex-col sm:flex-row justify-between items-start sm:items-center">
                                <span class="font-semibold text-gray-500 dark:text-gray-400 mb-1 sm:mb-0">09.30 - 10.15</span>
                                <div class="text-left sm:text-right">
                                    <span class="font-bold text-om-navy dark:text-white block">MATEMATIKA WAJIB</span>
                                    <span class="text-[10px] font-normal text-gray-500 dark:text-gray-400 block">Jefry Corpry YH</span>
                                </div>
                            </li>
                            <li class="p-2 rounded bg-om-cream/70 dark:bg-om-navy/40 flex flex-col sm:flex-row justify-between items-start sm:items-center">
                                <span class="font-semibold text-gray-500 dark:text-gray-400 mb-1 sm:mb-0">10.15 - 11.00</span>
                                <div class="text-left sm:text-right">
                                    <span class="font-bold text-om-navy dark:text-white block">PKN</span>
                                    <span class="text-[10px] font-normal text-gray-500 dark:text-gray-400 block">Agus Salim</span>
                                </div>
                            </li>
                            <li class="p-2 rounded bg-om-cream/70 dark:bg-om-navy/40 flex flex-col sm:flex-row justify-between items-start sm:items-center">
                                <span class="font-semibold text-gray-500 dark:text-gray-400 mb-1 sm:mb-0">11.00 - 11.45</span>
                                <div class="text-left sm:text-right">
                                    <span class="font-bold text-om-navy dark:text-white block">PKN</span>
                                    <span class="text-[10px] font-normal text-gray-500 dark:text-gray-400 block">Agus Salim</span>
                                </div>
                            </li>
                            <li class="p-2 rounded bg-amber-500/10 text-amber-700 dark:text-amber-300 flex justify-between items-center font-bold">
                                <span>11.45 - 12.30</span>
                                <span>ISTIRAHAT</span>
                            </li>
                            <li class="p-2 rounded bg-om-cream/70 dark:bg-om-navy/40 flex flex-col sm:flex-row justify-between items-start sm:items-center">
                                <span class="font-semibold text-gray-500 dark:text-gray-400 mb-1 sm:mb-0">12.30 - 13.15</span>
                                <div class="text-left sm:text-right">
                                    <span class="font-bold text-om-navy dark:text-white block">B. INGGRIS</span>
                                    <span class="text-[10px] font-normal text-gray-500 dark:text-gray-400 block">Yuli Hastuti</span>
                                </div>
                            </li>
                            <li class="p-2 rounded bg-om-cream/70 dark:bg-om-navy/40 flex flex-col sm:flex-row justify-between items-start sm:items-center">
                                <span class="font-semibold text-gray-500 dark:text-gray-400 mb-1 sm:mb-0">13.15 - 13.55</span>
                                <div class="text-left sm:text-right">
                                    <span class="font-bold text-om-navy dark:text-white block">B. INGGRIS</span>
                                    <span class="text-[10px] font-normal text-gray-500 dark:text-gray-400 block">Yuli Hastuti</span>
                                </div>
                            </li>
                            <li class="p-2 rounded bg-om-cream/70 dark:bg-om-navy/40 flex flex-col sm:flex-row justify-between items-start sm:items-center">
                                <span class="font-semibold text-gray-500 dark:text-gray-400 mb-1 sm:mb-0">13.55 - 14.35</span>
                                <div class="text-left sm:text-right">
                                    <span class="font-bold text-om-navy dark:text-white block">B. INGGRIS</span>
                                    <span class="text-[10px] font-normal text-gray-500 dark:text-gray-400 block">Yuli Hastuti</span>
                                </div>
                            </li>
                            <li class="p-2 rounded bg-om-cream/70 dark:bg-om-navy/40 flex flex-col sm:flex-row justify-between items-start sm:items-center">
                                <span class="font-semibold text-gray-500 dark:text-gray-400 mb-1 sm:mb-0">14.35 - 15.15</span>
                                <div class="text-left sm:text-right">
                                    <span class="font-bold text-om-navy dark:text-white block">EKONOMI</span>
                                    <span class="text-[10px] font-normal text-gray-500 dark:text-gray-400 block">Debie Lola</span>
                                </div>
                            </li>
                        </ul>
                    </div>

                    <!-- JUMAT -->
                    <div class="day-card rounded-2xl bg-om-card-light dark:bg-om-card-dark border border-om-gold/30 p-6 shadow-xl" data-day-name="JUMAT">
                        <div class="flex items-center justify-between border-b border-om-gold/20 pb-3 mb-4">
                            <h3 class="font-serif text-xl font-bold text-om-navy dark:text-om-gold flex items-center gap-2">
                                <i class="fa-solid fa-mosque text-sm"></i> JUMAT
                            </h3>
                            <span class="text-[10px] uppercase font-bold px-2 py-0.5 rounded bg-om-gold/20 text-om-gold">Jadwal Sekolah</span>
                        </div>
                        <ul class="space-y-2 text-xs">
                            <li class="p-2 rounded bg-blue-500/10 text-blue-700 dark:text-blue-300 flex flex-col sm:flex-row justify-between items-start sm:items-center font-bold">
                                <span class="mb-1 sm:mb-0">06.30 - 07.15</span>
                                <span class="sm:text-right">Jumat Bersih/ Sehat/<br>Literasi/ Ekspresi/ Public Speaking</span>
                            </li>
                            <li class="p-2 rounded bg-om-cream/70 dark:bg-om-navy/40 flex flex-col sm:flex-row justify-between items-start sm:items-center">
                                <span class="font-semibold text-gray-500 dark:text-gray-400 mb-1 sm:mb-0">07.15 - 08.00</span>
                                <div class="text-left sm:text-right">
                                    <span class="font-bold text-om-navy dark:text-white block">PKWU</span>
                                    <span class="text-[10px] font-normal text-gray-500 dark:text-gray-400 block">Debie Lola</span>
                                </div>
                            </li>
                            <li class="p-2 rounded bg-om-cream/70 dark:bg-om-navy/40 flex flex-col sm:flex-row justify-between items-start sm:items-center">
                                <span class="font-semibold text-gray-500 dark:text-gray-400 mb-1 sm:mb-0">08.00 - 08.45</span>
                                <div class="text-left sm:text-right">
                                    <span class="font-bold text-om-navy dark:text-white block">PKWU</span>
                                    <span class="text-[10px] font-normal text-gray-500 dark:text-gray-400 block">Debie Lola</span>
                                </div>
                            </li>
                            <li class="p-2 rounded bg-amber-500/10 text-amber-700 dark:text-amber-300 flex justify-between items-center font-bold">
                                <span>08.45 - 09.15</span>
                                <span>ISTIRAHAT</span>
                            </li>
                            <li class="p-2 rounded bg-om-cream/70 dark:bg-om-navy/40 flex flex-col sm:flex-row justify-between items-start sm:items-center">
                                <span class="font-semibold text-gray-500 dark:text-gray-400 mb-1 sm:mb-0">09.15 - 10.00</span>
                                <div class="text-left sm:text-right">
                                    <span class="font-bold text-om-navy dark:text-white block">PJOK</span>
                                    <span class="text-[10px] font-normal text-gray-500 dark:text-gray-400 block">Sopyan</span>
                                </div>
                            </li>
                            <li class="p-2 rounded bg-om-cream/70 dark:bg-om-navy/40 flex flex-col sm:flex-row justify-between items-start sm:items-center">
                                <span class="font-semibold text-gray-500 dark:text-gray-400 mb-1 sm:mb-0">10.00 - 10.45</span>
                                <div class="text-left sm:text-right">
                                    <span class="font-bold text-om-navy dark:text-white block">PJOK</span>
                                    <span class="text-[10px] font-normal text-gray-500 dark:text-gray-400 block">Sopyan</span>
                                </div>
                            </li>
                            <li class="p-2 rounded bg-om-cream/70 dark:bg-om-navy/40 flex flex-col sm:flex-row justify-between items-start sm:items-center">
                                <span class="font-semibold text-gray-500 dark:text-gray-400 mb-1 sm:mb-0">10.45 - 11.30</span>
                                <div class="text-left sm:text-right">
                                    <span class="font-bold text-om-navy dark:text-white block">B. KONSELING</span>
                                    <span class="text-[10px] font-normal text-gray-500 dark:text-gray-400 block">Katarina</span>
                                </div>
                            </li>
                            <li class="p-2 rounded bg-emerald-500/10 text-emerald-700 dark:text-emerald-400 flex justify-between items-center font-bold">
                                <span>11.30 - 12.30</span>
                                <span>JUMAT IBADAH</span>
                            </li>
                            <li class="p-2 rounded bg-amber-500/10 text-amber-700 dark:text-amber-300 flex justify-between items-center font-bold">
                                <span>12.30 - 13.00</span>
                                <span>ISTIRAHAT</span>
                            </li>
                            <li class="p-2 rounded bg-om-cream/70 dark:bg-om-navy/40 flex flex-col sm:flex-row justify-between items-start sm:items-center">
                                <span class="font-semibold text-gray-500 dark:text-gray-400 mb-1 sm:mb-0">13.00 - 13.45</span>
                                <div class="text-left sm:text-right">
                                    <span class="font-bold text-om-navy dark:text-white block">GEOGRAFI</span>
                                    <span class="text-[10px] font-normal text-gray-500 dark:text-gray-400 block">Nur Fajar Sidik</span>
                                </div>
                            </li>
                            <li class="p-2 rounded bg-om-cream/70 dark:bg-om-navy/40 flex flex-col sm:flex-row justify-between items-start sm:items-center">
                                <span class="font-semibold text-gray-500 dark:text-gray-400 mb-1 sm:mb-0">13.45 - 14.30</span>
                                <div class="text-left sm:text-right">
                                    <span class="font-bold text-om-navy dark:text-white block">GEOGRAFI</span>
                                    <span class="text-[10px] font-normal text-gray-500 dark:text-gray-400 block">Nur Fajar Sidik</span>
                                </div>
                            </li>
                        </ul>
                    </div>

                </div>'''

pattern = re.compile(r'<!-- GRID OF DAYS -->\s*<div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">.*?</div>\s*</div>\s*</div>\s*<!-- PART 2: MY SCHEDULE -->', re.DOTALL)
new_content, count = pattern.subn(new_html + '\n            </div>\n\n            <!-- PART 2: MY SCHEDULE -->', content)
if count > 0:
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(new_content)
    print("Successfully replaced the grid.")
else:
    print("Could not find the target section to replace.")
