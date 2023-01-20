SELECT (CAST(date_trunc('week', ("Data - FkData"."DataCompleta" + (INTERVAL '1 day'))) AS timestamp) + (INTERVAL '-1 day')) AS "Data - FkDataDataCompleta", "Saude Local - FkLocal"."Estado" AS "Saude Local - FkLocalEstado", sum("public"."saude_fatos"."Registro_ocorrencia") AS "sum"
FROM "public"."saude_fatos"
LEFT JOIN "public"."data" "Data - FkData" ON "public"."saude_fatos"."fkData" = "Data - FkData"."pkData" LEFT JOIN "public"."saude_local" "Saude Local - FkLocal" ON "public"."saude_fatos"."fkLocal" = "Saude Local - FkLocal"."pkLocal"
WHERE (("Data - FkData"."Semana" = '1'
    OR "Data - FkData"."Semana" = '2' OR "Data - FkData"."Semana" = '3' OR "Data - FkData"."Semana" = '4' OR "Data - FkData"."Semana" = '5')
   AND "Data - FkData"."Ano" = '2021')
GROUP BY (CAST(date_trunc('week', ("Data - FkData"."DataCompleta" + (INTERVAL '1 day'))) AS timestamp) + (INTERVAL '-1 day')), "Saude Local - FkLocal"."Estado"
ORDER BY (CAST(date_trunc('week', ("Data - FkData"."DataCompleta" + (INTERVAL '1 day'))) AS timestamp) + (INTERVAL '-1 day')) ASC, "Saude Local - FkLocal"."Estado" ASC